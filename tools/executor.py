import os
import subprocess
from threading import Lock

file_lock = Lock()


def write_file(path: str, content: str):

    try:

        directory = os.path.dirname(path)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with file_lock:

            with open(
                path,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(content)

        return {
            "success": True,
            "message": f"File written: {path}",
            "path": path
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


def run_python(path: str):

    try:

        result = subprocess.run(
            ["python", path],
            capture_output=True,
            text=True,
            timeout=60
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


def run_shell(command: str):

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }