import cmd

from src.cmd_built_in import cd
import src.parsing
import subprocess

built_in = ["cd", "if", "for"]


def exec_simple(cmd_simple):
    space = " "
    cmd_simple["args"] = space.join(cmd_simple["args"])
    cmd_built_in = None

    if cmd_simple["cmd"] in built_in:
        if (cmd_simple["cmd"] == "cd"):
            cmd_built_in = ["python3", "src/cmd_built_in/cd.py"] + cmd_simple["args"]
        if (cmd_simple["cmd"] == "if"):
            cmd_built_in = ["python3", "src/cmd_built_in/if.py"] + cmd_simple["args"]

        if(cmd_simple["stdout"]):
            with open(cmd_simple["stdout"]["filename"], cmd_simple["stdout"]["mode"]) as f:
                proc = subprocess.Popen(cmd_built_in, stdout= f)
                proc.wait()
        elif (cmd_simple["stdin"]):
            with open(cmd_simple["stdin"]["filename"]) as f:
                proc = subprocess.Popen(cmd_built_in, stdin=f)
                proc.wait()

    else:
        if (cmd_simple["stdout"]):
            subprocess.Popen(cmd_simple["cmd"],cmd_simple["args"], stdout=cmd_simple["stdout"]["filename"])

