# 1
import queue
import copy
from collections import deque

def odometer(oksana: list) -> int:
    dist: int = 0
    for i in range(0,len(oksana),2):
        if i == 0:
            dist = oksana[i] * oksana[i + 1]
        else:
            dist += oksana[i] * ( oksana[i + 1] - oksana[i - 1])
    return dist

# заменил массив из микса времени и расстояний на две очереди с временными интервалами и расстояниями
# для этого данные должны приходить в более удобном для рассчета виде

def odometer(time_intervals: queue, const_speed_values: queue) -> int:

    time_intervals_copy = copy.deepcopy(time_intervals)
    const_speed_values_copy = copy.deepcopy(const_speed_values)

    if time_intervals_copy.qsize() != const_speed_values.qsiz():
        raise ValueError("queue sizes should match")

    distance: int = 0
    while not time_intervals_copy.empty():
        distance += time_intervals_copy.get() * const_speed_values_copy.get()
    return distance

# 2
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

def MadMax2(N: int, Tele: list) -> list:
    l_sorted = Sorting_private(Tele)

    # для учебной задачи упростил только часть функции. Используя очередь обращаюсь к элементам массива только последовательно,
    # что улучшает читабельность и позволяет не следить за сложными выражениями в качестве индексов
    # использую очередь как стек, для инвертирования второй части списка
    decreasing_deque = deque()

    for i in range(N // 2, N):
        decreasing_deque.append(l_sorted[i])

    for i in range(N // 2, N):
        l_sorted[i] = decreasing_deque.pop()

    return l_sorted

# 3
def Unmanned(L: int, N: int, track: list) -> int:
# Определяем количество светофоров на пути
    num_of_traf = 0
    for elem in track:
        if elem[0] >= L:
            break
        num_of_traf += 1

    if num_of_traf == 0:
        return L
# Вычисляем время передвижения

# Время прохождения  до первого светофора включительно
    time = track[0][0] + Waitingtime(track[0][0], track[0])

# Время прохождения  до конца маршрута
    for i in range(1, num_of_traf):
        time += track[i][0] - track[i-1][0]
        time += Waitingtime(time, track[i])
    return time + L - track[num_of_traf-1][0]


def Waitingtime(time: int, regime: list) -> int:

    if time % sum(regime[1:]) - regime[1] < 0:
        return regime[1] - time % sum(regime[1:])
    return 0

# вместо использования списков, с непонятно как организованной информацией(по коду уже трудно разобраться, а условие к сожалению не сохранил),
# я бы подавал на вход две очереди: одна из которых содержит время или дистанцию до каждого светофора, а другая кортеж из режима зеленого и красного света

def Unmanned(L: int, distances_to_traflights: deque, lights_red_greed_times: deque) -> int:

    while distances_to_traflights:
        next_distance = distances_to_traflights.pop()
        red_waiting_time, green_wating_time = lights_red_greed_times.pop()
        #....


# 4
current_string = ""
all_states = []
position = -1
state = False


def BastShoe(command: str) -> str:

    if command[0] == "1":
        return Add(command[2:])

    if command[0] == "2":
        return Delete(int(command[2:]))

    if command[0] == "3":
        return Give(int(command[2:]))

    if command[0] == "4":
        return Undo()

    if command[0] == "5":
        return Redo()
    
def Undo() -> str:

    global position
    global state
    global current_string

    state = True

    if position == 0:
        return current_string
    
    position -= 1
    current_string = all_states[position]
    return all_states[position]
    
# вместо списка для хранения состояний, предлагаю использовать очередь, 
# которая будет работать как стек и добавлять/извлекать последнее состояние

current_string = ""
all_states = deque()

def Undo() -> str:
    if all_states:
        current_string = all_states.pop()
    return current_string

# 5

def TRC_sort(trc: list) -> list:

    if len(trc) < 2:
        return trc

    low = 0
    mid = 0
    hi = len(trc) - 1
    trc1 = [x for x in trc]
    order_sort(trc1, low, mid, hi)

    return trc1


def order_sort(trc: list, low: int, mid: int, hi: int):

    if mid > hi:
        return None

    if trc[low] == 0:
        order_sort(trc, low + 1, mid + 1, hi)

    if trc[low] == 2:
        trc[low], trc[hi] = trc[hi], trc[low]
        order_sort(trc, low, mid, hi-1)

    if trc[low] == 1 and trc[mid] == 1:
        order_sort(trc, low, mid + 1, hi)

    if trc[low] == 1 and trc[mid] == 0:
        trc[low], trc[mid] = trc[mid], trc[low]
        order_sort(trc, low + 1, mid + 1, hi)
        
    if trc[low] == 1 and trc[mid] == 2:
        trc[mid], trc[hi] = trc[hi], trc[mid]
        order_sort(trc, low, mid, hi-1)

# со словарем задача решается нагляднее и безопаснее, хоть и менее эффективно с точки зрения памяти и количества проходов
def TRC_sort(trc: list) -> list:

    count_dict = {0: 0, 1: 0, 2: 0}
    for element in trc:
        count_dict[element] += 1
    sorted_list = [0] * count_dict[0] + [1] * count_dict[1] + [2] * count_dict[2]

    return sorted_list