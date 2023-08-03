def Even_index(list1: list) -> None:

    if len(list1) == 0:
        return None

    print(list1[0])
    
    if len(list1) > 1:
        Even_index(list1[2:])
    return None
