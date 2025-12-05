from src.parsing.tokenizer import tokenizer
from src.parsing.parser import parse
from src.execution.executor_simple import exec_simple
from src.execution.exec_pipeline import exec_pipe
from src.utils.background import background_processes
from src.utils.handle_builtins import handle_builtin
import os

BLUE = "\033[94m"
RESET = "\033[0m"


def main():
    while True:
        for p in background_processes[:]:
            state = p.poll()
            if state is not None:
                print(f"[{p.pid}] finish (status {state})")
                background_processes.remove(p)

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

        if cmd["type"] == "command":
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
