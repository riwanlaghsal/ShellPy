import cmd

from src.cmd_built_in import cd
import src.parsing
import subprocess

built_in = ["cd", "if", "for"]


def exec_simple(cmd_simple):
    space = " "
    cmd_simple[args] = space.join(cmd_simple[args])
    if cmd_simple[cmd] in built_in:
        if(cmd_simple[stdin])
        subprocess.call(cmd_simple[cmd], cmd_simple[args[0]])
    else:

        subprocess.Popen(cmd_simple[cmd],cmd_simple[args[0]])

