def Even(list1: list) -> None:

    count = 0
    length = len(list1)
    Check(list1, count, length)


def Check(list1: list, count, length) -> None:
    if length == count:
        return None

    if list1[count] % 2 == 0:
        print(list1[count])

    return Check(list1, count + 1, length)
