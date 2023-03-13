def alphabet_position(text, alpha="abcdefghijklmnopqrstuvwxyz"):
    numbers = " ".join([str(alpha.index(l) + 1) for l in text.lower() if l in alpha])
    return numbers
