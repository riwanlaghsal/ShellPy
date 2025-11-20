from src.parsing.tokenizer import tokenizer
from src.parsing.parser import parse
from src.parsing.expand_var import expand_var
from src.execution.executor_simple import exec_simple
from src.cmd_built_in.cd import cd

import sys

PROMPT = "ShellPy$ "

def handle_builtin(cmd):
    """
    Gère les commandes internes (cd, exit).
    """
    if cmd["type"] != "command":
        return False

    if not cmd["cmd"]:
        return False

    if cmd["cmd"] == "cd":
        # cd argument
        arg = cmd["args"][0] if cmd["args"] else None
        cd(arg)
        return True

    if cmd["cmd"] == "exit":
        code = int(cmd["args"][0]) if cmd["args"] else 0
        sys.exit(code)

    return False


def main():
    while True:
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

        # 1) Tokenisation
        tokens = tokenizer(line)

        # 2) Parsing
        cmd = parse(tokens)

        # 3) Expansion variables ($HOME ...)
        # Dans ton code, expand_var fonctionne sur les tokens, donc :
        if isinstance(cmd, dict) and "cmd" in cmd:
            new_tokens = expand_var([cmd["cmd"]] + cmd["args"])
            cmd["cmd"] = new_tokens[0]
            cmd["args"] = new_tokens[1:]

        # 4) Builtins
        if handle_builtin(cmd):
            continue

        # 5) Exécution des commandes externes
        try:
            exec_simple(cmd)
        except Exception as e:
            print("Erreur d'exécution :", e)


if __name__ == "__main__":
    main()
