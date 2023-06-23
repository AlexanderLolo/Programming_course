def Sorting_private(list1: list) -> list:
    xchange = True
    res_list = []
    for i in list1:
        res_list.append(i)

    while xchange:
        xchange = False
        for i in range(len(res_list)-1):
            if res_list[i] > res_list[i+1]:
                res_list[i], res_list[i+1] = res_list[i+1], res_list[i]
                xchange = True
    return res_list

def MadMax(N: int, Tele: list) -> list:
    l_sorted = Sorting_private(Tele)
    for i in range((N - N // 2) // 2 ):
        l_sorted[N // 2 +i], l_sorted[N-1-i] = l_sorted[N-i-1], l_sorted[N // 2 +i]

    return l_sorted
