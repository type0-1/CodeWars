def add_length(str_):
    str_ = str_.strip().split()
    for i, word in enumerate(str_):
        str_[i] = str_[i] + " " + str(len(str_[i]))
    return str_
