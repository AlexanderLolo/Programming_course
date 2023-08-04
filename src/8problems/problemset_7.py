def Secondmax(list1: list) -> int:

    if len(list1) < 2:
        return None

    maxi = max(list1[0], list1[1])
    mini = min(list1[0], list1[1])
    del list1[0:2]

    return Recurrent(list1, maxi, mini)


def Recurrent(list1: list, max1: int, max2: int) -> int:

    if len(list1) == 0:
        return max2

    if list1[0] > max1:
        max2 = max1
        max1 = list1[0]

    if list1[0] > max2:
        max2 = list1[0]

    del list1[0:1]

    return Recurrent(list1, max1, max2)
