# Goal was to return result of the power of number "p" times without the use of utilities or **

def number_to_pwr(number, p):
    first = number
    list = [number for i in range(p - 1)]
    for n in list:
        number *= n
    return number if p != 0 else 1
