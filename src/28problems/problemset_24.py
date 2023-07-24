def MatrixTurn(matrix: list, M: int, N: int, T: int):
    # function rotates matrix clockwise

    for k in range(min(M, N)//2-1, -1, -1):
        # selecting a layer starting from the center

        temp = [matrix[k+i][k:M-k] for i in range(N-2*k)]

        # rotating this layer T Times
        for _ in range(T):
            RotateLayer(temp, M-2*k, N-2*k)
        
        # updating matrix with new layer
        for i in range(N-2*k):
            matrix[k+i] = matrix[k+i][:k] + temp[i] + matrix[k+i][M-k:]


def RotateLayer(matrix: list, M: int, N: int):
    # function rotates an outward layer 

    temp = [string[:] for string in matrix]

    matrix[0] = temp[1][0] + temp[0][:-1]
    matrix[N-1] = temp[N-1][1:] + temp[N-2][-1]

    for i in range(1, N-1):
        matrix[i] = temp[i+1][0]+temp[i][1:M-1]+temp[i-1][-1]
