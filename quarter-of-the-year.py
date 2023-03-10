def quarter_of(month):
    months = []
    for i in range(0, 12):
        months.append(((((i // 3)) + 1), i + 1))
    return [tup[0] for tup in months if tup[1] == month][0]
        
