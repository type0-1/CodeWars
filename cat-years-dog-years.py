def human_years_cat_years_dog_years(human_years, cat=0, dog=0):
    returnValue = human_years
    
    while human_years != 0:
        if human_years == 1:
            cat += 15
            dog += 15
        elif human_years == 2:
            cat += 9
            dog += 9
        else:
            cat += 4
            dog += 5
        human_years -= 1
    
    return [returnValue, cat, dog]
        
        
