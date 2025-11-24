import os

shell_state = {
    "?": 0, #last exit code (cmd exit + int change cette valeur)
    "$": os.getpid(), #pid du processus du shell
    "0": "ShellPy" #nom du shell
}