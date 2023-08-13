def EEC_help(arr1: list, arr2: list) -> bool:

    if len(arr1) != len(arr2):
        return False

    dict1 = {}
    for element in arr1:
        if element not in dict1:
            dict1[element] = 1
        else:
            dict1[element] += 1

    dict2 = {}

    for element in arr2:
        if element not in dict2:
            dict2[element] = 1
        else:
            dict2[element] += 1

    return dict1 == dict2
