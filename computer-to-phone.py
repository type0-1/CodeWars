def computer_to_phone(numbers, board=["0", "7", "8", "9", "4", "5", "6", "1", "2", "3"]):
    return "".join([str(board.index(i)) for i in numbers])
