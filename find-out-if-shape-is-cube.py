def cube_checker(volume, side):
    if volume <= 0 and side <= 0:
        return False
    else:
        if (side ** 3) == volume:
            return True
    return False
