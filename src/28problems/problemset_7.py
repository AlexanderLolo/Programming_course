def StringSplit(leng: int, string1: str) -> list:

    if len(string1) == 0:
        return []

    list1 = string1.rstrip().split()
    list2 = []
    position = 0
    curr_len = 0

    for i, el in enumerate(list1):

        if i == 0 and len(el) <= leng:
            list2.append(el)
            curr_len = len(el)

        elif curr_len + len(el) + 1 <= leng:
            list2[position] += " " + el
            curr_len += len(el) + 1

        elif len(el) > leng:
            for j in range(len(el) // leng):
                if i != 0 :
                    position += 1
                list2.append(el[j*leng: j*leng +leng])
                
            if len(el) % leng != 0:
                position += 1
                list2.append(el[len(el) - len(el) % leng:])
            curr_len = len(el) % leng

        else:
            position += 1
            curr_len = len(el)
            list2.append(el)
            
    return list2

def WordSearch(leng: int, string1: str, subs: str) -> list:
    list1 = StringSplit(leng, string1)
    list2 = []

    for strl in list1:
        if strl.startswith(subs + " ") or strl.endswith(" " + subs) or " " + subs + " " in strl or subs == strl:
            list2.append(1)
        else:
            list2.append(0)
    return list2
