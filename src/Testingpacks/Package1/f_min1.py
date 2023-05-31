import logging

logging.basicConfig(filename='../../Modules_and_packs.log', level=logging.DEBUG, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

# посмотрю, как мои исключения будут влиять на работоспособность программы
def min1(m, flag):  # True - возвращает минимальный элемент из массива, False - возвращает номер минимального элемента в массиве

    try:
        if not isinstance(m, list):
            raise TypeError("Ошибка: в функцию min1 должен быть передан список")

        logging.info(f"min1: значение флага передаваемого в функцию - {flag}, список состоит из {len(m)} элементов")
        logging.debug(f"min1: Начинаем проверку сравниваемых элементов на корректность")
        for i in range(len(m)):
            if isinstance(m[i], float):
                raise TypeError("Ошибка: предаваемый функции min1 список элементов должен состоять из целых чисел")
            elif not isinstance(m[i], int):
                raise TypeError("Ошибка: предаваемый функции min1 список элементов должен состоять из чисел")

        if not isinstance(flag, bool):
            raise TypeError("Ошибка: второй аргумент функции min1 должен быть True или False")

        logging.debug("min1: корректность сравниваемых элементов подтверждена")

        if len(m) == 0:
            logging.debug("min1: в списке не оказалось элементов для сравнения")
            return None

        for i in range(len(m)):
            if i == 0:
                minel = m[i]
                count = 0

            elif m[i] < minel:
                minel = m[i]
                count = i

        logging.info(f"min1: минимальный элемент равен {minel}, его номер в списке {count + 1} ")
        assert count >= 0 and count <= len(m) # индекс не можетбыть больше длины списка, будет явно абсурдная ситуация

        if flag:
            return minel
        else:
            return count + 1

    except TypeError as error:
        print(error)
        logging.exception(error)
    return None
