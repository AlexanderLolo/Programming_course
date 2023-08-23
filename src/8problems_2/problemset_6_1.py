def TRC_sort(trc: list) -> list:

    indicator = [0, 0, 0]

    for element in trc:
        indicator[element] += 1

    trc1 = []

    for i in range(3):
        trc1 += [i]*indicator[i]

    return trc1
