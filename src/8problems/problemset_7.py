def Secondmax(list1: list) -> int:

    if len(list1) < 2:
        return None

    index = 2
    length = len(list1)

    maxi = max(list1[0], list1[1])
    mini = min(list1[0], list1[1])

    return Recurrent(list1, index, length, maxi, mini)


def Recurrent(list1: list, index, length, max1: int, max2: int) -> int:

    if length == index:
        return max2

    if list1[index] > max1:
        max2 = max1
        max1 = list1[index]

    elif list1[index] > max2:
        max2 = list1[index]

    return Recurrent(list1, index + 1, length, max1, max2)
