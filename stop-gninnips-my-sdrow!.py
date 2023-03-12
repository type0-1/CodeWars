def spin_words(sentence, final= ""):
    if len(sentence) > 1:
        sentence = sentence.strip().split()
        for i, word in enumerate(sentence):
            if len(word) <= 4:
                final += word + " "
            else:
                final += word[::-1] + " "
        return final.strip()
    else:
        return sentence[::-1]
    return None
