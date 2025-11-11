def tokenize(line):
    line = line.strip()
    tokens = []
    current = ""
    inside_quotes = False
    i = 0
    while i < len(line):
        c = line[i]

        # rencontre de guillemet
        if c == '"':
            if inside_quotes: # si on est deja dans une string interne c le dernier "
                tokens.append(current)
                current = ""
                inside_quotes = False
            else: # sinon on met inside_quotes à true
                if current != "":
                    tokens.append(current)
                    current = ""
                inside_quotes = True
            i += 1
            continue

        if inside_quotes:
            current += c
            i += 1
            continue

        if c.isspace():
            if current != "":
                tokens.append(current)
                current = ""
            i = i+1
            continue

        # redirection append
        if c == '>' and i + 1 < len(line) and line[i+1] == '>':
            if current != "":
                tokens.append(current)
                current = ""
            tokens.append(">>")
            i += 2
            continue

        # redirections simples, pipes, ou &
        if c in ['>', '<', '|', '&']:
            if current != "":
                tokens.append(current)
                current = ""
            tokens.append(c)
            i += 1
            continue

        # caractère normal
        current += c
        i+= 1

    if current != "":
        tokens.append(current)

    return tokens





line = "echo ""bonjour"" >> test.txt   "
print(tokenize(line))
