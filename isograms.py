def is_isogram(string):
    string = string.lower()
    for s in string:
        if string.count(s) > 1:
            return False
    return True
