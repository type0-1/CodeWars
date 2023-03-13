def longest(a1, a2="", new=""):
    if len(a1) > 1:
        for s in a1:
            if s not in new:
                new += s
    if len(a2) > 1:
        for s in a2:
            if s not in new:
                new += s
    return "".join(sorted(new))
    
