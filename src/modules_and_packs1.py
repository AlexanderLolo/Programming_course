from Testingpacks.Package1 import f_min1
from Testingpacks.Package2 import f_palindrom1

import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename='Modules_and_packs.log', level=logging.DEBUG, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

# функция предназначена для создания списка из трех чисел, введенных с консоли
def threedigitlist():
    try:
        print("введите три целых числа")
        a = []
        for i in range(3):
            n = int(input("введите число"))
            a.append(n)
        assert len(a) == 3
        return a

    except ValueError as err:
        print("threedigit: Некорректные данные. Допустимо ввести только целые числа")
        logging.exception(err)
    return None

# демонстрирую, как мои исключения будут влиять на работоспособность программы
for i in range(10):
    b = threedigitlist()

    result = f_palindrom1.minpalicheck(b)
    logging.info(f"результат получился типа {type(result)}, попытка ввода номер {i + 1}")

    if result is None:
        print('у вас осталось', 10 - i - 1, "попыток")
    else:
        break

if result is None:
    print("перезапустите программу")
elif result:
    print("минимальное число является палиндромом")
else:
    print("минимальное число не является палиндромом")
