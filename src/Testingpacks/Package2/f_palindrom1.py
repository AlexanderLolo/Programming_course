from Testingpacks.Package1 import f_min1
import logging

logging.basicConfig(filename='../../Modules_and_packs.log', level=logging.DEBUG, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

# все функции в случае ошибок у меня возвращают None
def palindrom(num):
    try:
        logging.info(f"palindrom: число {num} проверяется на принадлежность к классу палиндромов")
        if isinstance(num, float):
            raise TypeError("Ошибка: аргумент функции Palindrom должен быть целым")  # должен быть return?
        elif not isinstance(num, int):
            raise TypeError("Ошибка: аргумент функции Palindrom должен быть числом")
        elif num < 0:
            raise ValueError("Ошибка: аргумент функции Palindrom должен быть неотрицительным")

        n = num
        rev = 0
        while n != 0:
            d = n % 10
            rev = rev * 10 + d
            n = n // 10
            assert rev < num * 10 # число наоборот не может быть в 10 раз больше
        assert isinstance(rev, int) # и не может быть другого типа
        logging.info(f"palindrom: построенное обратное число к {num}, это {rev}")
        return num == rev

    except ValueError as error:
        logging.exception(error)
    except TypeError as error:
        logging.exception(error)

    return None # можно было и не указывать, но для наглядности.. 


def minpalicheck(b):
    c = f_min1.min1(b, True)
    logging.info(f"minpalicheck: на палиндром будет проверяться число {c}")
    return palindrom(c)
