import sys
from src.parsing.parser import parse

def builtin_for(cmd_struct):
    args = cmd_struct["args"]
    var_name = args[0]

    if len(args) < 4:
        print("Erreur syntaxe: for <var> in ... do ... done", file=sys.stderr)
        return False

    if args[1] != "in":
        print(f"Erreur syntaxe: attendu 'in',, reçu '{args[1]}'", file=sys.stderr)
        return False



