def MassVote(N: int, votes: list) -> str:

    vmax = max(votes)

    if votes.count(vmax) > 1:
        return "no winner"

    if round(vmax / sum(votes), 3) <= 0.5:
        return "minority winner {}".format(votes.index(vmax)+1)

    return "majority winner {}".format(votes.index(vmax)+1)
