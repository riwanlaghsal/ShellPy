import shlex
import os
import re
from src.parsing.expand_var import expand_var


ALERT_TAG = "__NO_EXPAND__"
def put_alert(line):
    return re.sub(r"'([^']*\$[^']*)'", lambda m: ALERT_TAG + m.group(1) + ALERT_TAG, line)

def restore_alert(tokens):
    return [t.replace(ALERT_TAG, "") for t in tokens]


def tokenizer(line):
    line = line.replace('|', ' | ')
    line = re.sub(r'(>>|>|<)', r' \1 ', line)
    line = put_alert(line)
    tokens = shlex.split(line)
    # print(tokens)
    tokens = expand_var(tokens)
    return restore_alert(tokens)

# line = "echo bjr>>test.txt>fichier|ls '$name'"
# print(tokenizer(line))
