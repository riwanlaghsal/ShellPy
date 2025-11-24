import os

def expand_var(tokens):
    new_tokens = []
    for token in tokens:
        if token.startswith("'") and token.endwith("'"):
            new_tokens.append(token)
        elif token.startswith("$"):
            var_name = token[1:]
            value = os.environ.get(var_name, "")
            new_tokens.append(value) # pas de gestion d'erreur comme un vrai shell (ex: echo n'affiche rien)
        else:
            new_tokens.append(token)
    return new_tokens