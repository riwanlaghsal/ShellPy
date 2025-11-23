import shlex
import os
from src.parsing.expand_var import expand_var

def tokenizer(line):
    line = line.replace(">", " > ")
    line = line.replace(">>", " >> ")
    line = line.replace("<", " < ")
    line = line.replace("|", " | ")
    tokens = shlex.split(line)
    tokens = expand_var(tokens)
    return tokens

# line = "echo bjr>test.txt|ls"
# print(tokenizer(line))
