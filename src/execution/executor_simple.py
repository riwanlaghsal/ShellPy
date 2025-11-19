# from ShellPy.src.cmd_built_in.cd import cd
import subprocess
from redir import handle_redir
import os
import sys

def get_path(cmd_simple):
    path = str(cmd_simple["args"])
    path = path[2:-2]
    return path

def exec_simple(cmd_simple):
    built_in = ["cd", "if", "for"]
    cmd_built_in = None

    stdin, stdout = handle_redir(cmd_simple)
    if stdin == -1:
        return -1
    commande = [cmd_simple["cmd"]] + cmd_simple["args"]

    if cmd_simple["cmd"] in built_in:
        if (cmd_simple["cmd"] == "cd"):
            path = get_path(cmd_simple)
            cd(path)
        if (cmd_simple["cmd"] == "if"):
            cmd_built_in = ["python3", "../cmd_built_in/if.py"] + cmd_simple["args"]

    else:
        try:
            proc = subprocess.Popen(commande, stdin=stdin, stdout=stdout)
            proc.wait()
        except FileNotFoundError:
            print("Erreur : commande introuvable", file=sys.stderr)

simple_cmd = {
    "type": "command",
    "cmd": "cat",
    "args": [],
    "stdin": {"file": "test"},
    "stdout": None,
    "background": False
}
exec_simple(simple_cmd)
# print(os.getcwd())
