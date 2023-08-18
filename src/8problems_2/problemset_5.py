def massdriver(activate):

    index = len(activate)
    dict1 = {}

    for i, element in enumerate(activate):

        if element not in dict1:
            dict1[element] = i

        elif dict1[element] < index:
            index = dict1[element]

    if index < len(activate):
        return index
    return -1
