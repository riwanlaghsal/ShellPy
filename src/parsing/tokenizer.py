import shlex
import os
from expand_var import expand_var

def tokenizer(line):
    tokens = shlex.split(line)
    tokens = expand_var(tokens)
    return tokens

# line = "echo $LANG"
# print(tokenizer(line))
