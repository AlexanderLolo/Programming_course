def Secondmax(list1: list) -> int:

    if len(list1) < 2:
        return None

    return Recurrent(list1[2:], max(list1[0], list1[1]), min(list1[0], list1[1]))


def Recurrent(list1: list, max1: int, max2: int) -> int:

    if len(list1) == 0:
        return max2

    if list1[0] > max1:
        max2 = max1
        max1 = list1[0]

    if list1[0] > max2:
        max2 = list1[0]

    return Recurrent(list1[1:], max1, max2)
