def EEC_help(arr1: list, arr2: list) -> bool:

    if len(arr1) != len(arr2):
        return False

    dict1 = {}
    for element in arr1:
        if element not in dict1:
            dict1[element] = 1
        else:
            dict1[element] += 1

    for element in arr2:
        if element not in dict1 or dict1[element] == 0:
            return False
        else:
            dict1[element] -= 1

    return True
