def Listlen(list1: list) -> int:
# List is being changed when function is called

    if len(list1) == 0:
        return 0

    list1.pop(0)
    return 1 + Listlen(list1)
