def xor(a,b):
    case1 = a == True
    case2 = b == True
    if case1 and case2:
        return False
    elif not(case1) and case2:
        return True
    elif case1 and not(case2):
        return True
    else:
        return False
