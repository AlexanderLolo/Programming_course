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

def SynchronizingTables(N: int, ids: list, salary: int) -> list:

    if N == 0 or N == 1:
        return salary
    dict_salary = {}
    sorted_ids = Sorting_private(ids)
    sorted_salary = Sorting_private(salary)

    for count, key in enumerate(sorted_ids):
        dict_salary[key] = sorted_salary[count]

    for count, key in enumerate(ids):
        sorted_salary[count] = dict_salary.get(key)

    return sorted_salary
