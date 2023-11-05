# 1, 2
#### было
def PatternUnlock(N: int, hits: list) -> str:

    if N == 1 or N == 0:
        return ""

    dict_code = {}
    dict_code.update({6: [1,1], 1: [1,2], 9: [1,3] , 5: [2,1], 2: [2,2], 8: [2,3], 4: [3,1], 3: [3,2], 7: [3,3]})

    dist = 0

    for key in range(N-1):
        if sum(dict_code.get(hits[key])) - sum(dict_code.get(hits[key+1])) in [1,-1]:
            dist += 1
        else:
            dist += 2 ** (0.5)

    dist = round(dist * 100_000)
    return str(dist).replace("0","")

#### стало
def PatternUnlock(N, hits):
    if N <= 1:
        return ""

    dict_code = {6: [1, 1], 1: [1, 2], 9: [1, 3], 5: [2, 1], 2: [2, 2], 8: [2, 3], 4: [3, 1], 3: [3, 2], 7: [3, 3]}
    dist = 0

    # Вычисление расстояния убираем в отдельную функию
    for key in range(N - 1):
        dist += calculate_distance(dict_code, hits[key], hits[key + 1])

    # Форматирование ответа убираем в отдельную функию
    return format_distance(dist)

def calculate_distance(dict_code, hit1, hit2):

    if sum(dict_code.get(hit1)) - sum(dict_code.get(hit2)) in [1, -1]:
        return 1
    else:
        return 2 ** 0.5

def format_distance(dist):

    dist = round(dist * 100_000)
    return str(dist).replace("0", "")

# 3
#### было

def TheRabbitsFoot(str1: str, encode: bool) -> str:

    string1 = str1.rstrip().replace(" ", "")

    if len(string1) == 0:
        return ""

    leng = len(string1)
    leng_sqrt = int(leng ** (1/2))

    if leng_sqrt ** 2 == leng:
        n_rows = leng_sqrt
        n_colomns = leng_sqrt

    elif leng_sqrt * (leng_sqrt + 1) >= leng:
        n_rows = leng_sqrt
        n_colomns = leng_sqrt + 1
    else:
        n_rows = leng_sqrt + 1
        n_colomns = leng_sqrt + 1

    if encode:
        return Encrypt(string1, n_colomns)
    return Decrypt(string1, n_colomns, n_rows)

#### стало
def TheRabbitsFoot(str1: str, encode: bool) -> str:

    string1 = str1.rstrip().replace(" ", "")

    if len(string1) == 0:
        return ""
    #### вычисление размерности выношу в отдельную функцию
    n_rows, n_colomns = get_dimensions(len(str1))
    if encode:
        return Encrypt(string1, n_colomns)
    return Decrypt(string1, n_colomns, n_rows)

def get_dimensions(leng):
    leng_sqrt = int(leng ** 0.5)
    if leng_sqrt ** 2 == leng:
        return leng_sqrt, leng_sqrt
    elif leng_sqrt * (leng_sqrt + 1) >= leng:
        return leng_sqrt, leng_sqrt + 1
    else:
        return leng_sqrt + 1, leng_sqrt + 1


# 4, 5
#### было
def PrintingCosts(str1: str) -> int:

    row_data = """(пробел) 0   !   9        "   6        #  24        $  29        %  22
                  &  24        '   3        (  12        )  12        *  17        +  13
                  ,   7        -   7        .   4        /  10        0  22        1  19
                  2  22        3  23        4  21        5  27        6  26        7  16
                  8  23        9  26        :   8        ;  11        <  10        =  14
                  >  10        ?  15        @  32        A  24        B  29        C  20
                  D  26        E  26        F  20        G  25        H  25        I  18
                  J  18        K  21        L  16        M  28        N  25        O  26
                  P  23        Q  31        R  28        S  25        T  16        U  23
                  V  19        W  26        X  18        Y  14        Z  22        [  18
                  \  10        ]  18        ^   7        _   8        `   3        a  23
                  b  25        c  17        d  25        e  23        f  18        g  30
                  h  21        i  15        j  20        k  21        l  16        m  22
                  n  18        o  20        p  25        q  25        r  13        s  21
                  t  17        u  17        v  13        w  19        x  13        y  24
                  z  19        {  18        |  12        }  18        ~   9 """
    dict1 = {}
    row_list = row_data.split()
    for i in range(0, len(row_list), 2):
        dict1[row_list[i]] = int(row_list[i+1])
    dict1[" "] = dict1.pop("(пробел)", 11)

    summ = 0
    for char in str1:
        summ += dict1.get(char, 23)

    return summ


#### стало
def PrintingCosts(str1: str) -> int:
    row_data = """(пробел) 0   !   9        "   6        #  24        $  29        %  22
                  &  24        '   3        (  12        )  12        *  17        +  13
                  ,   7        -   7        .   4        /  10        0  22        1  19
                  2  22        3  23        4  21        5  27        6  26        7  16
                  8  23        9  26        :   8        ;  11        <  10        =  14
                  >  10        ?  15        @  32        A  24        B  29        C  20
                  D  26        E  26        F  20        G  25        H  25        I  18
                  J  18        K  21        L  16        M  28        N  25        O  26
                  P  23        Q  31        R  28        S  25        T  16        U  23
                  V  19        W  26        X  18        Y  14        Z  22        [  18
                  \  10        ]  18        ^   7        _   8        `   3        a  23
                  b  25        c  17        d  25        e  23        f  18        g  30
                  h  21        i  15        j  20        k  21        l  16        m  22
                  n  18        o  20        p  25        q  25        r  13        s  21
                  t  17        u  17        v  13        w  19        x  13        y  24
                  z  19        {  18        |  12        }  18        ~   9 """

    cost_dict = create_cost_dict(row_data)
    return calculate_printing_cost(str1, cost_dict)

# создание словаря затрат выношу в отдельную функцию
def create_cost_dict(row_data):
    cost_dict = {}
    items = row_data.split()
    for i in range(0, len(items), 2):
        cost_dict[items[i]] = int(items[i+1])
    cost_dict[" "] = cost_dict.pop("(пробел)")
    return cost_dict

# вычисление затрат выношу в отдельную функцию
def calculate_printing_cost(text, cost_dict):
    summ = 0
    for char in text:
        summ += cost_dict.get(char, 23)
    return summ

# 6, 7
#### было
def MassVote(N: int, votes: list) -> str:

    vmax = max(votes)

    if votes.count(vmax) > 1:
        return "no winner"

    if round(vmax / sum(votes), 3) <= 0.5:
        return "minority winner {}".format(votes.index(vmax)+1)

    return "majority winner {}".format(votes.index(vmax)+1)

#### стало
def MassVote(N, votes):
    vmax = max(votes)

    if votes.count(vmax) > 1:
        return "no winner"

    winner_type = determine_winner_type(votes, vmax)
    winner_index = votes.index(vmax) + 1
    return winner_message(winner_type, winner_index)

# Определение типа победителя выношу в отдельную функцию
def determine_winner_type(votes, vmax):
    if round(vmax / sum(votes), 3) > 0.5:
        return "majority"
    return "minority"

# Оповещение о победителе выношу в отдельную функцию
def winner_message(winner_type, winner_index):
    return "{} winner {}".format(winner_type, winner_index)

# 8
#### было
def UFO(N: int, data: list, octal: bool) -> list:

    if octal:
        return [int(str(x), 8) for x in data]
    return [int(str(x), 16) for x in data]

#### стало
def UFO(N: int, data: list, octal: bool):
    if octal:
        base = 8
    else:
        base = 16

    return [convert_number(x, base) for x in data]

# конвертирование числа в другую систему выношу в отдельную функцию
def convert_number(number, base):
    return int(str(number), base)


# 9, 10, 11
#### было
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

#### стало
def Unmanned(L, N, track):

    num_of_traf = num_traffic_lights(L, track)
    if num_of_traf == 0:
        return L
    time = calculate_total_time(L, track, num_of_traf)
    return time + L - track[num_of_traf-1][0]

# выносим подсчет числа светофоров в отдельную функцию
def num_traffic_lights(L, track):

    num_of_traf = 0
    for elem in track:
        if elem[0] >= L:
            break
        num_of_traf += 1

# считаем время до первого светофора в отдельной функции
def calc_time_till_first_traf(track):
    return track[0][0] + Waitingtime(track[0][0], track[0])

# выношу подсчет времени в отдельную функцию
def calculate_total_time(L, track, num_of_traf):
    time = calc_time_till_first_traf(track)
    for i in range(1, num_of_traf):
        time += track[i][0] - track[i-1][0]
        time += Waitingtime(time, track[i])
    return time

# 12
#### было
def LineAnalysis(line: str) -> bool:

    if line == "*":
        return True

    splitted = line.split("*")[1:-1]
    return max(splitted) == min(splitted)

#### стало
def LineAnalysis(line):

    if line == "*":
        return True

    splitted = line.split("*")[1:-1]
    return all_elements_equal(splitted)

# проверку всех частей строки на одинаковость паттерна выношу в отдельную функцию
def all_elements_equal(elements):

    return max(elements) == min(elements)


# 13
#### было
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


def Add(add: str) -> str:

    global current_string
    global all_states
    global position
    global state

    if state:
        all_states = [current_string]
        position = 0
        state = False

    current_string += add
    all_states.append(current_string)
    position += 1

    return current_string

#### стало
# вместо глобальных переменных создал класс, который хранит эти переменные как атрибуты, причем атрибуты закрытые
class BastShoe:
    
    def __init__(self):
        self.__current_string = ""
        self.__all_states = []
        self.__position = -1
        self.__state = False

    def process_command(self, command: str) -> str:
        if command[0] == "1":
            return self.__add(command[2:])
        if command[0] == "2":
            return self.__delete(int(command[2:]))
        if command[0] == "3":
            return self.__give(int(command[2:]))
        if command[0] == "4":
            return self.__undo()
        if command[0] == "5":
            return self.__redo()

    def __add(self, add: str) -> str:
        if self.__state:
            self.__all_states = [self.__current_string]
            self.__position = 0
            self.__state = False

        self.__current_string += add
        self.__all_states.append(self.__current_string)
        self.__position += 1
        return self.__current_string
    
# 14
#### было
class Node:

    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None

#### стало
#### делаю поля класса приватными и ввожу геттеры и сеттеры
class Node:

    def __init__(self, v):
        self.__value = v
        self.__next = None
        self.__prev = None

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev
    
    def set_value(self, v):
        self.__value = v
    
    def set_next(self, n):
        self.__next = n

    def set_prev(self, p):
        self.__prev = p

# 15
#### было
def MatrixTurn(matrix: list, N: int, M: int, T: int):
    # function rotates matrix clockwise

    for k in range(min(M, N)//2-1, -1, -1):
        # selecting a layer starting from the center

        temp = [matrix[k+i][k:M-k] for i in range(N-2*k)]

        # rotating this layer T Times
        for _ in range(T):
            RotateLayer(temp, N-2*k, M-2*k)
        
        # updating matrix with new layer
        for i in range(N-2*k):
            matrix[k+i] = matrix[k+i][:k] + temp[i] + matrix[k+i][M-k:]

#### стало
# выделил три этапа в три отдельные функции
def MatrixTurn(matrix, N, M, T):
    for layer_num in range(min(M, N)//2-1, -1, -1):
        layer = get_layer(matrix, M, N, layer_num)
        rotate_layer(layer, T)
        set_layer(matrix, layer, M, N, layer_num)

def get_layer(matrix, M, N, layer):

    return [matrix[layer+i][layer:M-layer] for i in range(N-2*layer)]

def rotate_layer(layer, times, layer_num):

    for _ in range(times):
        RotateLayer(layer, N-2*layer_num, M-2*layer_num)


def set_layer(matrix, layer, M, N, layer_num):

    for i in range(N-2*layer_num):
        matrix[layer_num+i] = matrix[layer_num+i][:layer_num] + layer[i] + matrix[layer_num+i][M-layer_num:]