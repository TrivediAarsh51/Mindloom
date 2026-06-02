import json
from pathlib import Path

TASK_FILE = Path("workspace/project_state/tasks.json")
TASK_FILE.parent.mkdir(parents=True, exist_ok=True)

class TaskGraph:
    def __init__(self):
        if not TASK_FILE.exists():
            TASK_FILE.write_text("[]")

    def load(self):
        return json.loads(TASK_FILE.read_text())

    def save(self, tasks):
        TASK_FILE.write_text(json.dumps(tasks, indent=4))

    def add_task(self, name, depends_on=None):
        tasks = self.load()
        tasks.append({
            "task": name,
            "depends_on": depends_on or [],
            "status": "pending"
        })
        self.save(tasks)

    def next_task(self):
        tasks = self.load()
        for t in tasks:
            if t["status"] != "pending":
                continue
            if all(self._done(dep, tasks) for dep in t["depends_on"]):
                return t
        return None

    def _done(self, name, tasks):
        for t in tasks:
            if t["task"] == name:
                return t["status"] == "done"
        return False

    def complete(self, name):
        tasks = self.load()
        for t in tasks:
            if t["task"] == name:
                t["status"] = "done"
        self.save(tasks)