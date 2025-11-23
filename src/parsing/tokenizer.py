import shlex
import os
import re
from src.parsing.expand_var import expand_var

def tokenizer(line):
    line = line.replace('|', ' | ')
    line = re.sub(r'(>>|>|<)', r' \1 ', line)
    tokens = shlex.split(line)
    tokens = expand_var(tokens)
    return tokens

# line = "echo bjr>>test.txt>fichier|ls"
# print(tokenizer(line))
