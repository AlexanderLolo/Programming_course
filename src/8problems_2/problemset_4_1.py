# Функция ниже, очевидно, является неэффективным решением и вообще не тем решением, которое предполагается для этой задачи.
# Хотя формально укладывается в ограничения по памяти и временную сложность(пусть и с таким огромным коэффициентом как 32000)

def artificial_muscle_fibers(arr: list) -> int:

    num = 0
    for i in range(1, 32000):
        count = 0
        for element in arr:
            if i == element:
                count += 1
            if count > 1:
                num += 1
                break

    return num

# За один проход сумел определить кол-во уникальных элементов в массиве.
# Для подсчета кол-ва дублируемых, даже в этом случае не хватает еще одного состояния, которое бы сигнализировало, что элемент встретился один или более раз.

# def artificial_muscle_fibers(arr: list) -> int:

    # bank = bytearray(4000)  # sys.getsizeof(a) == 4057
    # count = 0               # sys.getsizeof(32000) == 28

    # for element in arr:
    #     if bank[element // 8] & 1 << element % 8 == 0b0:
    #         bank[element // 8] = bank[element // 8] | 1 << element % 8
    #         count += 1

    # return count