def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:

    if N == 0 or M == 0:
        return 1

    # field creation
    field = []
    for i in range(N):
        y_axes = []
        for j in range(M):
            y_axes.append(False)
        field.append(y_axes)
    
    # field initialization during day 1
    days: int  = 1
    count: int = 0
    for i in range(L):
        if not field[battalion[2*i]-1][battalion[2*i+1]-1]:
            field[battalion[2*i]-1][battalion[2*i+1]-1] = True
            count += 1

    # actions till win
    while count < N * M:
        for i in range(N):
            for j in range(M):
                if not field[i][j] and (j + 1 < M and field[i][j+1] or j - 1 >= 0 and field[i][j-1] or i + 1 < N and field[i+1][j] or i - 1 >= 0 and field[i-1][j]):
                    field[i][j] = True
                    count += 1
        days += 1
    return days

