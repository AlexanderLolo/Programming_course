def white_walkers(village: str) -> bool:

    summ = 0
    count = 0
    flag = False
    for char in village:

        if char == "=":
            count += 1

        if char.isdigit() and summ + int(char) == 10:
            summ = int(char)
            flag = True
            if count == 3:
                count = 0
                continue
            return False
        
        elif char.isdigit():
            summ = int(char)
            count = 0
    return flag
