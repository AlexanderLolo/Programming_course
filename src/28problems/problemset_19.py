def ShopOLAP(N: int, items: list) -> bool:

    dict1 = {}

    for item in items:
        elem = item.split()
        if elem[0] not in dict1:
            dict1[elem[0]] = int(elem[1])
        else:
            dict1[elem[0]] += int(elem[1])

    lst = []
    for s in sorted(set(dict1.values()), reverse=True):
        keys = []
        for k in dict1:
            if dict1.get(k) == s:
                keys.append(k)

        for k in sorted(keys):
            lst.append(k + " " + str(s))

    return lst
