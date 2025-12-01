import sys
from src.cmd_built_in import cd
from src.utils.shell_state import shell_state

def handle_builtin(cmd):

    if cmd["type"] != "command":
        return False

    if not cmd["cmd"]:
        return False

    if cmd["cmd"] == "cd":
        arg = cmd["args"][0] if cmd["args"] else None
        cd(arg)
        return True

    if cmd["cmd"] == "exit":
        code = int(cmd["args"][0]) if cmd["args"] else 0
        # shell_state["?"] = code
        sys.exit(code)

    return False