geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    global geese
    birds = [animal for animal in birds if animal not in geese]
    return birds
