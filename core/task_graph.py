import json
from pathlib import Path
from threading import Lock

TASK_FILE = Path("workspace/project_state/tasks.json")
TASK_FILE.parent.mkdir(parents=True, exist_ok=True)

class TaskGraph:

    def __init__(self):
        self.lock = Lock()

        if not TASK_FILE.exists():
            TASK_FILE.write_text("[]")

    def load(self):
        with self.lock:
            return json.loads(TASK_FILE.read_text())

    def save(self, tasks):
        with self.lock:
            TASK_FILE.write_text(
                json.dumps(tasks, indent=4)
            )

    def add_task(self, name, depends_on=None):
        tasks = self.load()

        # Prevent duplicate tasks
        for task in tasks:
            if task["task"] == name:
                return

        tasks.append({
            "task": name,
            "depends_on": depends_on or [],
            "status": "pending"
        })

        self.save(tasks)

    def get_ready_tasks(self):

        tasks = self.load()

        ready = []

        for task in tasks:

            if task["status"] != "pending":
                continue

            if all(
                self._done(dep, tasks)
                for dep in task["depends_on"]
            ):
                ready.append(task)

        return ready

    def claim_task(self, task_name):

        tasks = self.load()

        for task in tasks:

            if (
                task["task"] == task_name
                and task["status"] == "pending"
            ):
                task["status"] = "running"
                self.save(tasks)
                return True

        return False

    def complete(self, task_name):

        tasks = self.load()

        for task in tasks:

            if task["task"] == task_name:
                task["status"] = "done"

        self.save(tasks)

    def fail(self, task_name):

        tasks = self.load()

        for task in tasks:

            if task["task"] == task_name:
                task["status"] = "failed"

        self.save(tasks)

    def has_pending_tasks(self):

        tasks = self.load()

        return any(
            t["status"] in ["pending", "running"]
            for t in tasks
        )

    def _done(self, name, tasks):

        for task in tasks:

            if task["task"] == name:
                return task["status"] == "done"

        return False