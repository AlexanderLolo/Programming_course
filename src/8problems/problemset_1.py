def Power(N: int, M: int) -> int:
# assume that if N == 0, then M can not be negative

    if M == 0:
        return 1

    if N == 0:
        return 0

    if M > 0:
        return N * Power(N, M - 1)

    return 1 / N * Power(N, M + 1)
