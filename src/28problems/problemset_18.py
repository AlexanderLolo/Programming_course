def MisterRobot(N: int, list1: list) -> bool:

    reverse = 0

    for i in range(N):
        for j in range(i+1, N):
            if list1[i] >= list1[j]:
                reverse += 1

    return reverse % 2 == 0
