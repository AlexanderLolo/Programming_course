def Unmanned(L: int, N: int, track: list) -> int:

    if N == 0:
        return L

    time = track[0][0] + Waitingtime(track[0][0], track[0])

    for i in range(1, N):
        time += track[i][0] - track[i-1][0]
        time += Waitingtime(time, track[i])
    return time + L - track[-1][0]


def Waitingtime(time: int, regime: list) -> int:

    if time % sum(regime[1:]) - regime[1] < 0:
        return regime[1] - time % sum(regime[1:])
    return 0
