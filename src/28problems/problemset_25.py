def TransformTransform(alist: list, N: int) -> bool:

    return sum(Transform(Transform(alist, N), N * (N + 1) // 2)) % 2 == 0


def Transform(alist: list, N: int):

    return [max(alist[j:i+j+1]) for i in range(N) for j in range(N-i)]
