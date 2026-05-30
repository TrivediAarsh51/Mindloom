import os
import subprocess


def write_file(path: str, content: str):
    """
    Write content to a file.
    Creates directories automatically if needed.
    """

    try:
        directory = os.path.dirname(path)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "success": True,
            "message": f"File written: {path}"
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def run_python(path: str):
    """
    Execute a Python file and capture output.
    """

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
    """
    Execute a shell command.
    """

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