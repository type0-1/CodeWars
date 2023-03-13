def duplicate_encode(word, output=""):
    word = word.lower()
    for l in word:
        if word.count(l) == 1:
            output += "("
        else:
            output += ")"
    return output
    
