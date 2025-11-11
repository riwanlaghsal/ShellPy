from ShellPy.src.parsing.tokenizer import tokenize

def parse_simple(tokens):
    simple_cmd = {
        "type": "command",
        "cmd": None,
        "args": [],
        "stdin": None,
        "stdout": None,
        "background": False
    }

    if tokens and tokens[-1] == "&":
        simple_cmd["background"] = True
        tokens = tokens[:-1]

    simple_cmd["cmd"] = tokens[0]
    i = 1

    while i < len(tokens):
        token = tokens[i]

        if token in [">", ">>"]:
            filename = tokens[i+1]
            simple_cmd["stdout"] = {"file": filename, "mode": "w"}
            i += 2
            continue

        if token == "<":
            filename = tokens[i+1]
            simple_cmd["stdin"] = filename
            i += 2
            continue

        simple_cmd["args"].append(token)
        i += 1
    return simple_cmd


def parse(tokens):
    return parse_simple(tokens)


line = "echo bonjour < salut.sh &"
tokens = tokenize(line)
print(parse(tokens))




