def squirrel(N: int):

    if N == 0:
        return 1
    fact: int = 1
    for i in range(1, N+1):
        fact *= i

    while fact // 10 != 0:
        fact = fact // 10

    return fact
