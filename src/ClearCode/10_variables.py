# 1, 2
def Sorting_private(list1: list) -> list:
    
    res_list = []
    for i in list1:
        res_list.append(i)

    xchange: bool = True # переменная теперь объявлена непосредственно перед циклом
    while xchange:
        xchange = False
        for i in range(len(res_list)-1):
            if res_list[i] > res_list[i+1]:
                res_list[i], res_list[i+1] = res_list[i+1], res_list[i]
                xchange = True
    xchange = None # Завершение работы с переменной
    return res_list

# 3,4 

def StringSplit(leng: int, string1: str) -> list:

    if len(string1) == 0:
        return []

    list1 = string1.rstrip().split()
    list2 = []
    position = 0
    # curr_len = 0 удаляю, так как присваивание значения произойдет непосредственно в цикле

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

    # Завершение работы с переменными
    position = -1
    curr_len = -1
            
    return list2

# 5
def BigMinus(str1: str, str2: str) -> str:

    if len(str1) > len(str2):
        maxstr = str1
        minstr = str2

    elif len(str1) < len(str2):
        maxstr = str2
        minstr = str1

    else:
        maxstr = max(str2, str1)
        minstr = min(str2, str1)

    if str1 == str2:
        return "0"
    
    result = MinusNumber(maxstr, minstr)

    # Завершение работы с переменными
    maxstr = "Error"
    mixstr = "Error"
    
    return result

# 6,7,8
def white_walkers(village: str) -> bool:

    # summ = 0 удаляю, так как присваивание значения произойдет непосредственно в цикле
    count = 0
    flag = False
    for char in village:

        if char == "=":
            count += 1
        
        digit = int(char)
        assert digit >= 0 and digit <= 9, "Wrong value" # проверяю на корректное значение

        if char.isdigit() and summ + int(char) == 10:

            summ = int(char)
            flag = True
            if count == 3:
                count = 0
                continue
            return False
        
        elif char.isdigit():
            summ = int(char)
            count = 0

    # Завершение работы с переменными
    count = -1
    summ = -1
    digit = -1
    
    return flag

# 9 
def Even_index(list1: list) -> None:

    index = 0
    length = len(list1)
    Print_even(list1, index, length)
    
    # Присваиваем невозможные значения
    index = -1
    length = -1

# 10
def EEC_help(arr1: list, arr2: list) -> bool:

    if len(arr1) != len(arr2):
        return False

    dict1 = {}
    for element in arr1:
        if element not in dict1:
            dict1[element] = 1
        else:
            dict1[element] += 1

    for element in arr2:
        if element not in dict1 or dict1[element] == 0:
            return False
        else:
            dict1[element] -= 1

    dict1 = None # завершаем работу со словарем
    return True

# 11, 12
def artificial_muscle_fibers(arr: list) -> int:

    bank = bytearray(4000)
    count = 0

    for element in arr:
        assert element >= 0 and element <= 31999, "Wrong number" # проверяю на корректное значение

        if bank[element // 8] & 1 << element % 8 == 0b0:
            bank[element // 8] = bank[element // 8] | 1 << element % 8
            count += 1
    bank = None # завершаю работу с массивом
    return count

# 13,14
def main():
    '''creates and prints a dictionnary with random keys and values '''

    dict_ = {}
    count = 1
    while count <= 100:
        key = random.randint(1, 1000)
        if key in dict_:
            continue
        val = str(random.randint(1, 1000000))
        dict_[key] = val
        i += count
    count = -1 # завершаю работу с аккумулятором

    for key in dict_:
        print(key, dict_.get(key))

    dict_ = None # завершаю работу со словарем

# 15  На примере ниже разобрался к каким ошибкам может привести инициализация поля класса не в конструкторе. 
# Хотя должны быть ситуации, когда это для чего-то нужно
class MyClass:
    # Поле класса, инициализированное не в конструкторе
    shared_list = []

    def __init__(self, value):
        self.value = value

    def add_to_shared_list(self, item):
        self.shared_list.append(item)

# Создание экземпляров класса
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

# Добавление значения в список для первого объекта
obj1.add_to_shared_list("Item from obj1")

# Вывода содержимого списка для второго объекта
print(obj2.shared_list)  # ['Item from obj1']