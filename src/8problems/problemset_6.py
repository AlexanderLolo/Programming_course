def Even_index(list1: list) -> None:

    index = 0
    length = len(list1)
    Print_even(list1, index, length)


def Print_even(list1: list, index, length) -> None:
    if length <= index:
        return None

    print(list1[index])

    return Print_even(list1, index + 2, length)
