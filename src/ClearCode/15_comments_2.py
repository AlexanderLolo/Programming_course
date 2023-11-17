# 1
def squirrel(N: int):

    if N == 0:
        return 1
    fact: int = 1
    for i in range(1, N+1):
        fact *= i

    # получение первой цифры факториала
    while fact // 10 != 0:
        fact = fact // 10

    # TO_DO - для N >= 100000 реализовать приближенное вычисление факториала с помощью формулы Стирлинга
    return fact

# 2

def sort_aggregated_data(aggr_data: dict) -> list:
    """
    TO_DO реализовать сортировку товаров по количеству продаж
    """
    pass

# 3, 4, 5

def odometer(oksana: list) -> int:
    """
    Вычисляет пройденное расстояние.
    Args:
        oksana: list: Список, содержащий скорости и время изменения скоростей [скорость1, время1, скросрость2, время2...]
    """
    # Важно: список должен содержать пары скорость-время, иначе вычисления будут некорректны (Предупреждение)
    # Правильное чередование скорости и времени критично для корректности  расчетов (Усиление)
    # TO_DO - Рассмотреть возможность добавления проверки входных данных

    dist: int = 0
    for i in range(0,len(oksana),2):
        if i == 0:
            dist = oksana[i] * oksana[i + 1]
        else:
            dist += oksana[i] * ( oksana[i + 1] - oksana[i - 1])
    return dist

# 6, 7, 8

def Sorting_private(list1: list) -> list:
    """
    Функция сортирует по возрастанию пузырьковым методом
    """
    # Пузырьковая сортировка используется для простоты реализации, несмотря на слабую эффективность (Намерение)
    # Важно: пузырьковая сортировка может быть неэффективна для больших списков ивыполняться долго, N > 1000000 (Предупреждение)
    # TO-DO рассмотреть оптимизацию функции и использование другого алгоритма при N > 1000000 
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

# 9, 10

def invert_list_from_position(list_to_invert: list, start_pos: int) -> list:
    """
    Инвертирует список, начиная с позиции start_pos с помощью стека
    """
    # Использование стэка обеспечивает безопасное инвертирование списка, исключая случаи выхода за рамками списка (Намерение)
    # TO_DO - Добавить проверку входных параметров на корректность (start_pos)

    decreasing_deque = deque()
    for i in range(start_pos, len(list_to_invert)):
        decreasing_deque.append(list_to_invert[i])

    for i in range(start_pos, len(list_to_invert)):
        list_to_invert[i] = decreasing_deque.pop()
    return list_to_invert


# 11

def PatternUnlock(N: int, hits: list) -> str:
    """"
    Функция вычисляет расстояние, между цифрами кода, переводит его в целое, оставляя пять знаков после запятой и избавляется от нулей.
    Последовательные цифры кода располагаются рядом друг с другом на клавиатуре.
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

    # Точность вычислений до 5 знака и удаление нулей в результате важны для правильного получения кода(Усиление)   
    dist = round(dist * 100_000)
    return str(dist).replace("0","")

# 12

def UFO(N: int, data: list, octal: bool) -> list:
    # TO_DO - реализовать алгоритм перевода из троичной системы счисления
    if octal:
        return [int(str(x), 8) for x in data]
    return [int(str(x), 16) for x in data]