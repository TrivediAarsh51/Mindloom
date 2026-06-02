from pathlib import Path
import subprocess

class TestRunner:
    def __init__(self, workspace="workspace"):
        self.workspace = Path(workspace)

    def run_tests(self):
        """
        Runs all Python files in workspace that start with test_*.py
        Returns list of results (success or errors)
        """
        results = []
        for file in self.workspace.glob("test_*.py"):
            try:
                completed = subprocess.run(
                    ["python", str(file)],
                    capture_output=True,
                    text=True,
                    check=True
                )
                results.append({"file": str(file), "output": completed.stdout, "success": True})
            except subprocess.CalledProcessError as e:
                results.append({"file": str(file), "output": e.stderr, "success": False})
        return results