import ast

from tools.executor import write_file, run_python, run_shell


def execute_tool_command(command: str):

    try:
        tree = ast.parse(command, mode="eval")

        call = tree.body

        func_name = call.func.id

        args = []

        for arg in call.args:
            args.append(ast.literal_eval(arg))

        if func_name == "write_file":
            return write_file(args[0], args[1])

        elif func_name == "run_python":
            return run_python(args[0])

        elif func_name == "run_shell":
            return run_shell(args[0])

        return f"Unknown tool: {func_name}"

    except Exception as e:
        return f"ERROR: {str(e)}"