def Even(list1: list) -> None:

    if len(list1) == 0:
        return None

    if list1[0] % 2 == 0:
        print(list1[0])

    del list1[0:1]
    Even(list1)
