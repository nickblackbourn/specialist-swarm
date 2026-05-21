"""
Patch the system prompts of the live coordinator + specialist agents in place.

Use after editing create_specialists.py or create_coordinator.py — pulls the
new prompts from those source files and updates the existing agents via
agents.update, so you don't have to re-create agents (which would orphan the
old IDs and break any session history references).

Idempotent: safe to run repeatedly. If the live prompt already matches the
source, the patch is a no-op.

Usage:
    python patch_agents.py
"""

import json
import os
from pathlib import Path

from anthropic import Anthropic

from create_specialists import SPECIALISTS
from create_coordinator import COORDINATOR_SYSTEM


def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("Set ANTHROPIC_API_KEY before running.")

    specialist_ids_path = Path(".specialist_ids.json")
    if not specialist_ids_path.exists():
        raise SystemExit("Run create_specialists.py first.")
    specialist_ids = json.loads(specialist_ids_path.read_text())

    coordinator_id_path = Path(".coordinator_id")
    if not coordinator_id_path.exists():
        raise SystemExit("Run create_coordinator.py first.")
    coordinator_id = coordinator_id_path.read_text().strip()

    client = Anthropic(
        default_headers={"anthropic-beta": "managed-agents-2026-04-01"},
    )

    print("Patching specialist system prompts...")
    for spec in SPECIALISTS:
        agent_id = specialist_ids.get(spec["key"])
        if not agent_id:
            print(f"  No agent ID for `{spec['key']}` in .specialist_ids.json — skipping")
            continue

        current = client.beta.agents.retrieve(agent_id)
        if current.system == spec["system"]:
            print(f"  {spec['name']:32s} already current — skipping")
            continue

        client.beta.agents.update(
            agent_id,
            version=current.version,
            system=spec["system"],
        )
        print(f"  {spec['name']:32s} patched ✓")

    print("\nPatching coordinator system prompt...")
    current = client.beta.agents.retrieve(coordinator_id)
    if current.system == COORDINATOR_SYSTEM:
        print(f"  Coordinator already current — skipping")
    else:
        client.beta.agents.update(
            coordinator_id,
            version=current.version,
            system=COORDINATOR_SYSTEM,
        )
        print(f"  Coordinator patched ✓")

    print("\nDone. Next: python upload_skills.py (if skills changed) then python run_deal_desk.py")


if __name__ == "__main__":
    main()
