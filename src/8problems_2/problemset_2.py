def digital_rain(col: str) -> str:

    if col.count("1") == len(col) or col.count("0") == len(col):
        return ""

    balance = 0
    dict1 = {0: -1}
    maxi = 0
    mini = 0

    for index, char in enumerate(col):
        if char == "1":
            balance += 1
        else:
            balance -= 1

        if balance in dict1.keys() and maxi - mini <= index - dict1[balance]:
            maxi = index
            mini = dict1[balance] + 1
        else:
            dict1[balance] = index

    return col[mini:maxi+1]
