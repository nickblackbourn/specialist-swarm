"""
Upload each skill in skills/ via the Skills API and attach to the right
agent (specialist or coordinator).

Uses `files_from_dir` (from anthropic.lib) to package the skill directory.
Each skill bundle must contain a SKILL.md at its root with proper YAML
frontmatter (`name` and `description`).

Idempotent:
  - If a skill with the same display_title already exists, a NEW VERSION
    is pushed via skills.versions.create. Agents reference version="latest"
    so they automatically pick up the new content.
  - If an agent already has the skill attached, the attachment step is
    skipped (no duplicate).

Usage:
    python upload_skills.py
"""

import json
import os
from pathlib import Path

from anthropic import Anthropic
from anthropic.lib import files_from_dir


# Specialist skills — attached to the matching specialist agent.
# Map: skill directory name → specialist key in .specialist_ids.json
SKILL_TO_SPECIALIST = {
    "pricing-playbook":   "pricing",
    "legal-checklist":    "legal",
    "competitive-intel":  "competitive",
    "solution-architect": "technical_fit",
}

# Coordinator skills — attached to the coordinator agent
# (whose ID is in .coordinator_id, not .specialist_ids.json).
COORDINATOR_SKILLS = {"win-strategy"}


def upload_or_version(client, skill_name, existing_by_title):
    """Upload a skill if new, or push a new version if it already exists.

    Returns the skill_id, or None if the skill directory is missing.
    """
    skill_dir = Path("skills") / skill_name
    if not (skill_dir / "SKILL.md").exists():
        print(f"  Skipping {skill_name} — no SKILL.md found")
        return None

    display_title = skill_name.replace("-", " ").title()
    files = files_from_dir(str(skill_dir))

    if display_title in existing_by_title:
        skill_id = existing_by_title[display_title]
        print(f"Pushing new version of: {skill_name} ({skill_id})...")
        client.beta.skills.versions.create(skill_id, files=files)
        print(f"  -> new version uploaded")
        return skill_id

    print(f"Creating new skill: {skill_name}...")
    skill = client.beta.skills.create(
        display_title=display_title,
        files=files,
    )
    print(f"  -> {skill.id}")
    return skill.id


def attach_skill(client, agent_id, agent_label, skill_id):
    """Attach a skill to an agent if not already attached. Idempotent."""
    print(f"  attaching to {agent_label} ({agent_id})...")
    current = client.beta.agents.retrieve(agent_id)
    # SDK returns skills as pydantic model objects, not dicts.
    existing_skills = list(current.skills or [])
    already_attached = any(
        getattr(s, "skill_id", None) == skill_id for s in existing_skills
    )
    if already_attached:
        print(f"  already attached ✓ (skipping)")
        return

    new_skills = [
        s.model_dump() if hasattr(s, "model_dump") else s
        for s in existing_skills
    ] + [{"type": "custom", "skill_id": skill_id, "version": "latest"}]
    client.beta.agents.update(
        agent_id,
        version=current.version,
        skills=new_skills,
    )
    print(f"  attached ✓")


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

    client = Anthropic()

    print("Checking for existing skills...")
    existing_by_title: dict[str, str] = {}
    for page in client.beta.skills.list(source="custom"):
        existing_by_title[page.display_title] = page.id

    uploaded: dict[str, str] = {}

    # Specialist skills
    for skill_name, specialist_key in SKILL_TO_SPECIALIST.items():
        skill_id = upload_or_version(client, skill_name, existing_by_title)
        if skill_id is None:
            continue
        uploaded[skill_name] = skill_id
        attach_skill(
            client,
            agent_id=specialist_ids[specialist_key],
            agent_label=f"specialist `{specialist_key}`",
            skill_id=skill_id,
        )

    # Coordinator skills
    for skill_name in COORDINATOR_SKILLS:
        skill_id = upload_or_version(client, skill_name, existing_by_title)
        if skill_id is None:
            continue
        uploaded[skill_name] = skill_id
        attach_skill(
            client,
            agent_id=coordinator_id,
            agent_label="coordinator",
            skill_id=skill_id,
        )

    Path(".skill_ids.json").write_text(json.dumps(uploaded, indent=2))
    print(f"\nUploaded/refreshed {len(uploaded)} skills.")
    print("Next: python patch_agents.py (if prompts changed) then python run_deal_desk.py")


if __name__ == "__main__":
    main()
