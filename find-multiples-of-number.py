def find_multiples(integer, limit):
    i = 1
    nums = []
    while i*integer <= limit:
        nums.append(i*integer)
        i += 1
    return nums
