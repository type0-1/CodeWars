def century(year):
    num, check = int(str(year)[:len(str(year)) // 2]), int(str(year)[len(str(year)) // 2:])
    print(num, check)
    if check < 1:
        return num
    elif year < 100:
        return 1
    else:
        return num + 1
