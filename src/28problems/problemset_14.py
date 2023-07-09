def Unmanned(L: int, N: int, track: list) -> int:
# Определяем количество светофоров на пути
    num_of_traf = 0
    for i in range(N):
        if track[i][0] >= L:
            break
        num_of_traf += 1

    if num_of_traf == 0:
        return L
# Вычисляем время передвижения

# Время прохождения  до первого светофора включительно
    time = track[0][0] + Waitingtime(track[0][0], track[0])

# Время прохождения  до конца маршрута
    for i in range(1, num_of_traf):
        time += track[i][0] - track[i-1][0]
        time += Waitingtime(time, track[i])
    return time + L - track[num_of_traf-1][0]


def Waitingtime(time: int, regime: list) -> int:

    if time % sum(regime[1:]) - regime[1] < 0:
        return regime[1] - time % sum(regime[1:])
    return 0
