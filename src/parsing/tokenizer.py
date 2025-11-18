import shlex
import os

def tokenizer(line):
    tokens = shlex.split(line)
    return tokens


# print(tokenizer(line))
