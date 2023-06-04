import logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

# list1 = [6, 2, 3]

def NotOptomizedSorting(list1):

    logging.debug(f"NotOptomizedSorting: в функцию передано значение типа - {type(list1)}")

    if not isinstance(list1, list):
        raise TypeError("В функцию можно передать только список")

    length = len(list1)
    logging.debug(f"NotOptomizedSorting: длина списка - {len(list1)}")

    for i in range(length):
        if not isinstance(list1[i], int):
            raise TypeError("Элементами списка могут быть только целые числа")
        
    logging.debug(f"NotOptomizedSorting: список до сортировки - {list1}")
    for j in range(length - 1): # последний элемент проверять не надо, он автоматически будет минимальным

        for i in range(length - j - 1): #ищем максимальный среди первых n-1 неупорядоченных элементов, если всего их на очередном шаге осталось n
            if i == 0:
                max = list1[i]   #нужен только номер максимального, поэтому переменная внутри цикла
                count = i
            elif list1[i] > max:
                max = list1[i]
                count = i
        if list1[count] > list1[length - 1 - j]:
            list1[count], list1[length - 1 - j] = list1[length - 1 - j], list1[count] #меняем очередной максимальный найденный на еще неупорядоченный с конца
        logging.debug(f"NotOptomizedSorting: список после {j+1} шага - {list1}")

    return list1

# print(NotOptomizedSorting(list1))
