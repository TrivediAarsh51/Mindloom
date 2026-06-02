from pathlib import Path

class ArchitectAgent:

    def generate_architecture(self, user_goal):
        architecture = f"""
# Mindloom v0.5 Architecture

Goal:
{user_goal}

Suggested Structure:

frontend/
backend/
database/
tests/
docs/

Core Components:

* API Layer
* Business Logic
* Database Layer
* Testing Layer
* Documentation Layer
"""

        state_dir = Path("workspace/project_state")
        state_dir.mkdir(parents=True, exist_ok=True)

        arch_file = state_dir / "architecture.md"
        arch_file.write_text(architecture)

        return architecture