def PatternUnlock(N: int, hits: list) -> str:

    if N == 1 or N == 0:
        return ""

    dict_code = {}
    dict_code.update({6: [1,1], 1: [1,2], 9: [1,3] , 5: [2,1], 2: [2,2], 8: [2,3], 4: [3,1], 3: [3,2], 7: [3,3]})

    dist = 0

    for key in range(N-1):
        if sum(dict_code.get(hits[key])) - sum(dict_code.get(hits[key+1])) in [1,-1]:
            dist += 1
        else:
            dist += 2 ** (0.5)

    dist = round(dist * 100_000)
    return str(dist).replace("0","")
