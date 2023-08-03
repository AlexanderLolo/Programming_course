def Palindrom(string1: str) -> bool:

    if len(string1) == 1 or len(string1) == 0:
        return True
    
    return Palindrom(string1[1:-1]) and string1[0] == string1[-1]
