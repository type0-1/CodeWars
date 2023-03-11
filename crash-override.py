def alias_gen(f_name, l_name):
    if not f_name[0].isalpha() or not l_name[0].isalpha():
        return 'Your name must start with a letter from A - Z.'
    else:
        code_name = []
        for letter in FIRST_NAME:
            if letter == f_name[0].upper():
                code_name.append(FIRST_NAME[letter])
        for letter in SURNAME:
            if letter == l_name[0].upper():
                code_name.append(SURNAME[letter])
        return " ".join(code_name)
                
            
