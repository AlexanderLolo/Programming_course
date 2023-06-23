def odometer(oksana: list) -> int:
    dist: int = 0
    for i in range(0,len(oksana),2):
        if i == 0:
            dist = oksana[i] * oksana[i + 1]
        else:
            dist += oksana[i] * ( oksana[i + 1] - oksana[i - 1])
    return dist
