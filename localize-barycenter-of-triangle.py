def bar_triang(point_a, point_b, point_c): 
    
    xA, yA = point_a[0], point_a[1]
    xB, yB = point_b[0], point_b[1]
    xC, yC = point_c[0], point_c[1]
    
    xO = round((xA + xB + xC) / 3, 4)
    yO = round((yA + yB + yC) / 3, 4)
    
    return [xO, yO]
    
