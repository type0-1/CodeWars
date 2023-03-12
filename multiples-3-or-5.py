def solution(number):
    list = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0 and i not in list:
            list.append(i)
    return sum(list)
