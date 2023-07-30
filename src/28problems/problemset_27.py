def Football(flist: list, N: int) -> bool:

    fordered = sorted(flist)

    if fordered == flist or N == 1:
        return False

    diff = list(map(lambda x, y: 1 if x-y != 0 else 0, flist, fordered))

    if diff.count(1) == 2:
        return True

    lower = diff.index(1)
    upper = N - diff[::-1].index(1)

    return fordered[lower:upper] == reversed(flist[lower:upper])
