def shortcut( s, vowels="aeiou" ):
    return "".join([c for c in s if c not in vowels])
