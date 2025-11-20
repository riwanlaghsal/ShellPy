import subprocess
import sys

from src.execution.redir import handle_redir
from src.execution.executor_simple import exec_simple

def exec_pipe(pipe):
    processus = []
    prev_stdout = None
    stdout_pipe = None
    built_in = ["cd", "if", "for"]

    for i, cmd in enumerate(pipe["commands"]):
        stdin, stdout = handle_redir(cmd)
        if prev_stdout:
            stdin = prev_stdout

        if i < len(pipe["commands"]) - 1:
            stdout_pipe = subprocess.PIPE
        else:
            stdout_pipe = stdout

        if cmd["cmd"] in built_in:
            exec_simple(cmd)
        else:
            commande = [cmd["cmd"]] + cmd["args"]
            try:
                proc = subprocess.Popen(commande, stdin=stdin, stdout=stdout_pipe)
                processus.append(proc)
                prev_stdout = proc.stdout
            except FileNotFoundError:
                print(f"Commande introuvable : {cmd['cmd']}", file=sys.stderr)
            finally:
                if stdin:
                    stdin.close()
                if stdout:
                    stdout.close()

    for proc in processus:
        proc.wait()


