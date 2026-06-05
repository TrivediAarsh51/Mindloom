import ast
import traceback

from tools.executor import (
    write_file,
    run_python,
    run_shell
)

ALLOWED_TOOLS = {
    "write_file": write_file,
    "run_python": run_python,
    "run_shell": run_shell
}


def execute_tool_command(command: str):

    try:

        tree = ast.parse(
            command,
            mode="eval"
        )

        if not isinstance(
            tree.body,
            ast.Call
        ):
            return {
                "success": False,
                "error": "Not a function call"
            }

        call = tree.body

        func_name = call.func.id

        if func_name not in ALLOWED_TOOLS:

            return {
                "success": False,
                "error": f"Unknown tool: {func_name}"
            }

        args = [
            ast.literal_eval(arg)
            for arg in call.args
        ]

        result = ALLOWED_TOOLS[
            func_name
        ](*args)

        return {
            "success": True,
            "tool": func_name,
            "args": args,
            "result": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }