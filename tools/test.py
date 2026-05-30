import sys
import os

# -------------------------------------------------
# FIX IMPORT PATH (VERY IMPORTANT FOR WINDOWS SETUP)
# -------------------------------------------------
sys.path.append(os.path.dirname(__file__))

# Now we can import from tools correctly
from executor import write_file, run_python, run_shell


# -------------------------------------------------
# 1. TEST FILE WRITING
# -------------------------------------------------
print("\n🧠 Testing file creation...")

file_path = "workspace/hello.py"
content = 'print("Hello from Mindloom Tool System!")'

result = write_file(file_path, content)
print(result)


# -------------------------------------------------
# 2. TEST PYTHON EXECUTION
# -------------------------------------------------
print("\n🚀 Testing Python execution...")

run_result = run_python(file_path)
print("STDOUT:")
print(run_result.get("stdout"))

print("STDERR:")
print(run_result.get("stderr"))


# -------------------------------------------------
# 3. TEST SHELL EXECUTION
# -------------------------------------------------
print("\n⚙️ Testing shell execution...")

shell_result = run_shell("echo Mindloom tool system working")
print("STDOUT:")
print(shell_result.get("stdout"))

print("STDERR:")
print(shell_result.get("stderr"))


# -------------------------------------------------
# DONE
# -------------------------------------------------
print("\n✅ ALL TOOL TESTS COMPLETED")