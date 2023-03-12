def get_count(sentence, vowels="aeiou"):
    return len([l for l in sentence if l in vowels])
