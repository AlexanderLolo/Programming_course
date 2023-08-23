def matrix(n: int, m: int, matrix1: list) -> list:

    result = []

    for k in range((m + 1) // 2):
        # selecting an external layer(matrix)
        temp = [matrix1[k+i][k:n-k] for i in range(m-2*k)]

        # making a list from external layer
        result += layer(n-2*k, m-2*k, temp)
    
    return result


def layer(n: int, m: int, matr: list) -> list:

    if n == 1:
        return [matr[i][0] for i in range(m)]
    
    if m == 1:
        return [matr[0][i] for i in range(n)]

    vert1 = []
    for i in range(1, m-1):
        vert1.append(matr[i][n-1])

    vert2 = []
    for i in range(m-2, 0, -1):
        vert2.append(matr[i][0])

    return matr[0] + vert1 + list(reversed(matr[m-1])) + vert2
