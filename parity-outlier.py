def find_outlier(integers):
    even = [n for n in integers if n % 2 == 0]
    odd = [n for n in integers if n % 2 != 0]
    if len(even) > 1:
        return odd[0]
    return even[0]
