# 1
class Node:

    def __init__(self, v):
        self.value = v ##### self.node_value
        self.next = None

# 2,3 
class DynArray:

    def __init__(self):
        self.count = 0 ##### num_array_elements
        self.capacity = 16 ##### max_array_capacity
        self.array = self.make_array(self.capacity)

# 4
def odometer(oksana: list) -> int:
    dist: int = 0 ##### distance_km
    for i in range(0,len(oksana),2):

# 5
def WordSearch(leng: int, string1: str, subs: str) -> list:
    list1 = StringSplit(leng, string1)
    list2 = [] ##### word_in_strings_flags

# 6,7
def PrintingCosts(str1: str) -> int:

    row_data = """(пробел) 0   !   9        "   6        #  24        $  29        %  22
 
    dict1 = {} ##### letters_codes_dict

    summ = 0
    for char in str1: summ += dict1.get(char, 23)

    return summ ##### toner_consumption

# 8
def MassVote(N: int, votes: list) -> str:

    vmax = max(votes) 
    ##### number_of_max_votes

# 9
def Unmanned(L: int, N: int, track: list) -> int:

    Определяем количество светофоров на пути
    num_of_traf = 0
    ...
    Время прохождения маршрута
    time = track[0][0] + Waitingtime(track[0][0], track[0]) 
    ##### time - rout_time_hrs


# 10, 11
def ShopOLAP(N: int, items: list) -> list:

    dict1 = {} ##### grouped_items_sales

    for item in items:
        elem = item.split()
        if elem[0] not in dict1:
            dict1[elem[0]] = int(elem[1])
        else:
            dict1[elem[0]] += int(elem[1])

    lst = [] ##### grouped_ordered_sales


# 12,13
def SherlockValidString(instr: str) -> bool:

    dict1 = {i: instr.count(i) for i in set(instr)} ##### num_letters_in_str
    set_ = set(dict1.values()) #####  set_of_unique_letters

# 14
def white_walkers(village: str) -> bool:

    summ = 0 ##### pair_digits_sum
    count = 0

# 15,16

def Recurrent(list1: list, index, length, max1: int, max2: int) -> int:

    if length == index:
        return max2  ##### second_max_number

    if list1[index] > max1: ##### max_number
        max2 = max1
        max1 = list1[index]
