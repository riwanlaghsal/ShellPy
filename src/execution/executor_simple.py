from main import handle_builtin
from src.cmd_built_in.cd import cd
import subprocess
from src.execution.redir import handle_redir
import os
import sys

def get_path(cmd_simple):
    path = str(cmd_simple["args"])
    path = path[2:-2]
    return path

def exec_simple(cmd_simple):
    built_in = ["cd", "if", "for", "exit"]
    cmd_built_in = None

    stdin, stdout = handle_redir(cmd_simple)
    if stdin == -1:
        return -1
    commande = [cmd_simple["cmd"]] + cmd_simple["args"]

    if cmd_simple["cmd"] in built_in:
        return handle_builtin(cmd_simple)

    else:
        try:
            proc = subprocess.Popen(commande, stdin=stdin, stdout=stdout)
            proc.wait()
        except FileNotFoundError:
            print(f"Erreur : commande '{cmd_simple['cmd']}' introuvable", file=sys.stderr)
        finally:
            if stdin:
                stdin.close()
            if stdout:
                stdout.close()
