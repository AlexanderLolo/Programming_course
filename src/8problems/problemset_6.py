def Even_index(list1: list) -> None:

    if len(list1) == 0:
        return None

    print(list1[0])
    
    if len(list1) > 1:
        del list1[0:2]
        Even_index(list1)
    return None
