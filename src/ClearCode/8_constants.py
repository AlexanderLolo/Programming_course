# Во всех примерах ввел константы весто машических чисел
# 1,2
class Equipment:

    def __init__(self, s, p):
        self._size = s
        self._tech_condition = 100 ##### DEFAULT_TECH_CONDITION = 100
        self._price = p
        self._aging_speed = 10 ##### DEFAULT_AGING_SPEED = 10

# 3,4
def PrintingCosts(str1: str) -> int:

    row_data = """(пробел) 0   !   9        "   6        #  24        $  29        %  22 """ ##### TONER_CONSUMP_TEMPL = " ..."

    dict1 = {}
    row_list = row_data.split()
    for i in range(0, len(row_list), 2):
        dict1[row_list[i]] = int(row_list[i+1])
    dict1[" "] = dict1.pop("(пробел)", 11)

    summ = 0
    for char in str1:
        summ += dict1.get(char, 23) #### VALUE_NOT_FOUND_CODE = 23

# 5,6
def MassVote(N: int, votes: list) -> str:

    vmax = max(votes)
    if votes.count(vmax) > 1:
        return "no winner"
    if round(vmax / sum(votes), 3) <= 0.5: #### ROUND_ACCURACY = 3  MINOR_WIN_THRESHOLD = 0.5
        return "minority winner {}".format(votes.index(vmax)+1)
    return "majority winner {}".format(votes.index(vmax)+1)

# 7,8
def artificial_muscle_fibers(arr: list) -> int:

    bank = bytearray(4000)  #### MAX_BUFFER_SIZE = 4000
    count = 0               

    for element in arr:
        if bank[element // 8] & 1 << element % 8 == 0b0: #### NUM_BITS_IN_BYTE = 8
            bank[element // 8] = bank[element // 8] | 1 << element % 8
            count += 1
    return count

# 9
# функция предназначена для создания списка из трех чисел, введенных с консоли
def threedigitlist():
    print("введите три целых числа")
    a = []
    for i in range(3): #### INPUT_NUMBERS_COUNT = 3
        n = int(input("введите число"))
        a.append(n)
    assert len(a) == 3
    return a

# 10
# демонстрирую, как мои исключения будут влиять на работоспособность программы
for i in range(10): #### NUM_OF_ATTEMPTS = 10
    b = threedigitlist()

    result = f_palindrom1.minpalicheck(b)
    logging.info(f"результат получился типа {type(result)}, попытка ввода номер {i + 1}")

    if result is None:
        print('у вас осталось', 10 - i - 1, "попыток")
    else:
        break

# 11, 12, 13
if len(list) != 3: #### NUM_INPUT_WORDS = 3
    logging.debug(f"строка {line} некорректна и будет пропущена(должно быть ровно три слова)")                 
elif int(list[1]) < 0 or int(list[1]) > 60: #### MAX_SPEED = 60
    logging.debug(f"строка {line} некорректна. Параметр скорости выходит за рамки допустимого") 
elif int(list[2]) < 0 or int(list[2]) > 300 : #### MAX_PURR_FREQ = 300
    logging.debug(f"строка {line} некорректна. Параметр частоты мурлыканья выходит за рамки допустимого")