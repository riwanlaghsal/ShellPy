from src.parsing.tokenizer import tokenizer
from src.parsing.parser import parse
from src.parsing.expand_var import expand_var
from src.execution.executor_simple import exec_simple
from src.cmd_built_in.cd import cd
from src.execution.exec_pipeline import exec_pipe
import os
import sys


# POUR L'INSTANT ON GERE LES BUILTINS ICI ON SUPPRIMERA CEUX DES EXEC ET ON DEPLACERA CELUI LA DANS UN FICHIER UTILS

BLUE = "\033[94m"
RESET = "\033[0m"

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
        sys.exit(code)

    return False


def main():
    while True:
        PROMPT = f"{BLUE}{os.getcwd()}{RESET}$ "
        try:
            line = input(PROMPT)
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()
            continue

        if not line.strip():
            continue

        tokens = tokenizer(line)

        cmd = parse(tokens)

        if handle_builtin(cmd):
            continue
        if (cmd["type"] == "command"):
            try:
                exec_simple(cmd)
            except Exception as e:
                print("Erreur d'exécution :", e)
        else:
            try:
                exec_pipe(cmd)
            except Exception as e:
                print("Erreur :", e)

if __name__ == "__main__":
    main()
