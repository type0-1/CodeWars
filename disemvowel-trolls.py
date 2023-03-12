def disemvowel(string_, vowels="aeiouAEIOU"):
    for s in string_:
        if s in vowels:
            string_ = string_.replace(s, "")
    return string_
