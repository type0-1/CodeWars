def kebabize(st, new=""):
    tmp = st
    for l in tmp:
        if l.isnumeric():
            pass
        elif l == l.upper() and l.upper() in tmp:
            new += "-" + l.lower()
        else:
            new += l.lower()
    if len(new) > 1:
        if new[0] == "-":
            return new[1:]
    return new
