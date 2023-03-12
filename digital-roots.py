def digital_root(n, total=0):
    n = sum(list(map(int, str(n))))
    if n <= 9:
        return n
    else:
        n = sum(list(map(int, str(n))))
        total = 0
        while n > 9:
            for i in str(n):
                total += int(i)
            n = total
        return n
