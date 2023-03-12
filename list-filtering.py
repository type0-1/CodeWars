def filter_list(l, final=[]):
    return [n for n in l if not isinstance(n, str)]
