def duplicate_count(text):
    dic = {}
    text = text.lower().strip()
    for s in text:
        if s not in dic and text.count(s) > 1:
            dic[s] = 1
    return len(dic)
