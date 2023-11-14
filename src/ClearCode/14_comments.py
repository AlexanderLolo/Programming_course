# 3.1.1
def squirrel(N: int):

    if N == 0:
        return 1
    fact: int = 1
    for i in range(1, N+1):
        fact *= i

    # получение первой цифры факториала
    while fact // 10 != 0:
        fact = fact // 10

    return fact

# мне, как еще пока новичку этот комментарий кажется полезным, так как помогает не думать что же за логика реализована. Хотя она и довольно проста,
# но по смыслу стоит отдельно от предыдущей, поэтому мозг ломается.Однако, если поставить цель избавиться от комментариев,
# то я бы ввел две новые функции с говорящими названиями

# 3.2.1
def factorial(N: int) -> int:
    """
    Вычисляем факториал числа N.
    """

    fact = 1
    for i in range(1, N + 1):
        fact *= i
    return fact

def first_digit(number: int) -> int:
    """
    Находим первую цифру числа.
    """

    while number // 10 != 0:
        number //= 10
    return number

def squirrel(N: int) -> int:
    """
    Возвращаем первую цифру факториала числа
    """

    fact = factorial(N)
    return first_digit(fact)


# 3.1.2
def odometer(oksana: list) -> int:
    """
    Вычисляет пройденное расстояние.
    Args:
        oksana: list: Список, содержащий скорости и время изменения скоростей [скорость1, время1, скросрость2, время2...]
    """
    # подсмотрел, что таким образом для функций пишут комментарии, помогающие понять входные данные и ее предназначение.
    # В виду сложности организации массива-аргумента, с чередующимися скоростями и временем изменения скоростей, думаю, что полезно.

    dist: int = 0
    for i in range(0,len(oksana),2):
        if i == 0:
            dist = oksana[i] * oksana[i + 1]
        else:
            dist += oksana[i] * ( oksana[i + 1] - oksana[i - 1])
    return dist

# 3.1.3

def Sorting_private(list1: list) -> list:
    """
    Функция сортирует по возрастанию пузырьковым методом
    """

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
    """
    Функция сортирует список по возрастанию, а затем вторую половину списка сортирует по убыванию
    """

    l_sorted = Sorting_private(Tele)
    for i in range((N - N // 2) // 2 ):
        l_sorted[N // 2 +i], l_sorted[N-1-i] = l_sorted[N-i-1], l_sorted[N // 2 +i]

    return l_sorted

# 3.2.2
# Для наглядности переименовываю и ввожу новую функцию[написал и понял, что этот комментарий бесполезен]
# Отрефакторенный вариант функций

def sort_ascending(list1: list) -> list:
    """
    Функция сортирует по возрастанию пузырьковым методом
    """

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

def invert_list_from_position(list_to_invert: list, start_pos: int) -> list:
    """
    Инвертирует список, начиная с позиции start_pos с помощью стека
    """

    decreasing_deque = deque()
    for i in range(start_pos, len(list_to_invert)):
        decreasing_deque.append(list_to_invert[i])

    for i in range(start_pos, len(list_to_invert)):
        list_to_invert[i] = decreasing_deque.pop()
    return list_to_invert

def MadMax(N: int, Tele: list) -> list:
    """
    Функция сортирует список по возрастанию, а затем вторую половину списка сортирует по убыванию
    """

    acs_sorted_list = sort_ascending(Tele)
    return invert_list_from_position(acs_sorted_list, N // 2 )

# 3.1.4

def PatternUnlock(N: int, hits: list) -> str:
    """"
    Функция вычисляет расстояние, между цифрами кода, переводит его в целое, оставляя пять знаков после запятой и избавляется от нулей.
    Последовательные цифры кода располагаются рядом другс другом на клавиатуре.
    Если друг под другом, то расстояние 1, если по диагонали, то sqrt(2).
    """

    if N == 1 or N == 0:
        return ""

    dict_code = {}

    # кодируем цифру ключа его координатой на клавиатуре
    dict_code.update({6: [1,1], 1: [1,2], 9: [1,3], 
                      5: [2,1], 2: [2,2], 8: [2,3], 
                      4: [3,1], 3: [3,2], 7: [3,3]})

    # вычисляем расстояние, между цифрами кода
    dist = 0
    for key in range(N-1):
        if sum(dict_code.get(hits[key])) - sum(dict_code.get(hits[key+1])) in [1,-1]:
            dist += 1
        else:
            dist += 2 ** (0.5)

    # обрабатываем результат надлежащим образом    
    dist = round(dist * 100_000)
    return str(dist).replace("0","")

# 3.2.3

def calc_key_distance(hits: list, N: int) -> float:
    """"
    Функция вычисляет расстояние, между цифрами кода.
    Последовательные цифры кода располагаются рядом другс другом на клавиатуре.
    Если друг под другом, то расстояние 1, если по диагонали, то sqrt(2).
    """
    dict_code = {}

    # кодируем цифру ключа его координатой на клавиатуре
    dict_code.update({6: [1,1], 1: [1,2], 9: [1,3], 
                      5: [2,1], 2: [2,2], 8: [2,3], 
                      4: [3,1], 3: [3,2], 7: [3,3]})
    
    # вычисляем расстояние, между цифрами кода
    dist = 0
    for key in range(N-1):
        if sum(dict_code.get(hits[key])) - sum(dict_code.get(hits[key+1])) in [1,-1]:
            dist += 1
        else:
            dist += 2 ** 0.5
    return dist

def convert_num_to_string(num: int) -> str:
 
    return str(num)

def remove_zeros_from_str(dist: str) -> str:

    return dist.replace("0", "")

def PatternUnlock(N: int, hits: list) -> str:

    if N <= 1:
        return ""
    
    distance = calc_key_distance(hits, N)
    rounded_dist = round(distance * 100_000)
    dist_string = convert_num_to_string(rounded_dist)

    return remove_zeros_from_str(dist_string)

# 3.1.5
# Несмотря на простоту функции, считаю, что комментарий полезен, так как сходу не сразу понимаешь для чего проверяется  условие

def SumOfThe(N: int, data: list) -> int:
    """
    Функция ищет число, которое является суммой всех других чисел в списке
    """

    for number in data:
        if sum(data) - number == number:
            return number
        
# 3.2.4
def find_balance_number(N: int, data: list) -> int:
    """
    Функция ищет число, которое является суммой всех других чисел в списке
    """

    total_sum = sum(data)

    for number in data:
        if  number * 2 == total_sum:
            return number
    return None

# 3.1.6/3.1.7

def ShopOLAP(N: int, items: list) -> list:
    """"
    Функция группирует продажи по названиям товаров, располагая в результирующем списке товары, 
    отсортированные по количеству продаж.
    """
    dict1 = {}

    # Группируем продажи по названию товаров
    for item in items:
        elem = item.split()
        if elem[0] not in dict1:
            dict1[elem[0]] = int(elem[1])
        else:
            dict1[elem[0]] += int(elem[1])

    # Сортируем товары по количеству продаж 
    lst = []
    for s in sorted(set(dict1.values()), reverse=True):
        keys = []
        for k in dict1:
            if dict1.get(k) == s:
                keys.append(k)

        for k in sorted(keys):
            lst.append(k + " " + str(s))

    return lst

# 3.2.5 для каждого смыслового блока заводим отдельную функцию с говорящим названием
def aggregate_sales_data(items: list) -> dict:
    """
    Группируем продажи по названию товаров
    """
    dict1 = {}
    for item in items:
        elem = item.split()
        if elem[0] not in dict1:
            dict1[elem[0]] = int(elem[1])
        else:
            dict1[elem[0]] += int(elem[1])
    return dict1

def sort_aggregated_data(aggr_data: dict) -> list:
    """
    Сортируем товары по количеству продаж
    """
    ...
    return sorted_list

def ShopOLAP(N: int, items: list) -> list:

    aggr_data = aggregate_sales_data(items)
    return sort_aggregated_data(aggr_data)