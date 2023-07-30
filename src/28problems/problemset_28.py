def Keymaker(N: int) -> str:

    list1 = [0 for _ in range(N)]

    for i in range(1, N + 1):
        for j in range(i, N + 1):
            if j % i == 0:
                list1[j-1] = (list1[j-1] + 1) % 2

    return "".join(map(str, list1))
