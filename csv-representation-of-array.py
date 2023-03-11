def to_csv_text(array):
    array = [",".join(list(map(str, arr))) for arr in array]
    s = ""
    for arr in array:
        s += arr + "\n"
    return s[:-1]
    # good luck
