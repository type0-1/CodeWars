def accum(s):
    strings = [(l[0].capitalize() + l[0:].lower() * i) for i, l in enumerate(s)]
    return "-".join(strings)
