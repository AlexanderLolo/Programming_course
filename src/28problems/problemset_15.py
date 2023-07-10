def TankRush(H1: int, W1: int, field1: str, H2: int, W2: int, field2: str) -> bool:

    if H2 > H1 or W2 > W1:
        return False
    
    S1 = field1.replace(" ", "")
    S2 = field2.replace(" ", "")

# ищем малый массив во всех строчках большого массива
    for i in range(H1-H2+1):
        if TankRushHelp(W1, S1[i*W1:], H2, W2, S2):
            return True
    return False


def TankRushHelp(W1: int, S1: str, H2: int, W2: int, S2: str) -> bool:
# ищем малый массив в первых H2 строчках большого массива
    if S1 == S2:
        return True
    
    for j in range(W1-W2+1):
        b = ""
        for i in range(j, H2*W1+j, W1):
            b += S1[i:i+W2]
        if b == S2:
            return True
    return False
