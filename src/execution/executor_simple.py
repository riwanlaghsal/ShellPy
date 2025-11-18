from ShellPy.src.cmd_built_in import cd
import subprocess
import redir
from ShellPy.src.execution.redir import handle_redir


def exec_simple(cmd_simple):
    built_in = ["cd", "if", "for"]
    cmd_built_in = None

    stdin, stdout = handle_redir(cmd_simple)
    if stdin == -1:
        return -1
    commande = [cmd_simple["cmd"]] + cmd_simple["args"]

    if cmd_simple["cmd"] in built_in:
        if (cmd_simple["cmd"] == "cd"):
            cmd_built_in = ["python3", "ShellPy/src/cmd_built_in/cd.py"] + cmd_simple["args"]
        if (cmd_simple["cmd"] == "if"):
            cmd_built_in = ["python3", "ShellPy/src/cmd_built_in/if.py"] + cmd_simple["args"]
        proc = subprocess.Popen(cmd_built_in, stdin=stdin, stdout=stdout)
        proc.wait()

    else:
        proc = subprocess.Popen(commande, stdin=stdin, stdout=stdout)
        proc.wait()

simple_cmd = {
    "type": "command",
    "cmd": "cd",
    "args": ["/src/parsing"],
    "stdin": None,
    "stdout": None,
    "background": False
}
import os
exec_simple(simple_cmd)
print(os.getcwd())