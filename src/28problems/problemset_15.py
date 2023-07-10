def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str,) -> bool:
    
    if H2 > H1 or W2 > W1:
        return False
    
    field1 = S1.split()
    field2 = S2.split()
    
    offset = 0
    for row2 in field2:
        if offset > H1:
            return False
        
        for i, row1 in enumerate(field1[offset:]):
            if row2 in row1:
                break
            if i == len(field1[offset:])-1:
                return False
        offset += i+1

    return True
