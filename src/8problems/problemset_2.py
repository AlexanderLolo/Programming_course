def Sumofnum(N: int) -> int:
# assume that  N >= 0. When N is negative we can take abs value

    if N // 10 == 0:
        return N

    return N % 10 + Sumofnum(N // 10)
