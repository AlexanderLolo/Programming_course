def TreeOfLife(H: int, W: int, N: int, plan: list) -> list:

    # converting to array consisting from 0s и 1s
    instr = [list(map(int, list(x.replace(".", "0").replace("+", "1")))) for x in plan]

    for i in range(N):

        instr = [[instr[k][m]+1 for m in range(W)] for k in range(H)]
        if i % 2 == 1:
            instr = Renew(H, W, instr)

    # converting to array consisting from "0" и "1"
    instr = list(map(lambda x: list(map(lambda z: "1" if z > 0 else "0", x)), instr))
    return ["".join(x).replace("0", ".").replace("1", "+") for x in instr]


def UpdateMatrix(H: int, W: int, i: int, j: int, matrix: list):

    for k, m in [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i, j)]:
        if k >= 0 and k < H and m >= 0 and m < W:
            matrix[k][m] = 0
    # return None  не уверен, что нужен, так как функция меняет входящий массив, а не возвращает что-то


def Renew(H: int, W: int, instr: list) -> list:

    matrix = [[1]*W for k in range(H)]

    for i in range(H):
        for j in range(W):
            if instr[i][j] >= 3:
                UpdateMatrix(H, W, i, j, matrix)

    return list(map(lambda x, y: list(map(lambda z, w: z * w, x, y)), instr, matrix))
