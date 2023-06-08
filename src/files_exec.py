import os
from random import randint
import logging

logging.basicConfig(filename='./Files_work_container/files_exec.log', level=logging.DEBUG, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


class FileIsNotCorrect(Exception):
    pass

def num_lines_in_file(file1, path):
    try:
        logging.debug(f"num_lines_in_file: попытка открыть файл {file1} в дирректории - {path}")
        with open(path + file1, "rt") as file:
            s = 0
            for line in file:
                s += 1
        logging.debug(f"num_lines_in_file: файл {file1} успешно открыт и прочитан, в нем {s} строк")
        return s
    except FileNotFoundError as e:
        print("num_lines_in_file: неверно указан путь или имя файла")
        logging.exception(e)

        
def sum_in_files(n1, n2, path):

    file1 = str(n1) + ".txt"
    file2 = str(n2) + ".txt"

    logging.debug(f"sum_in_files: суммируем значения по файлам {file1} и {file2}")

    try:
        for f in [file1, file2]:
            if num_lines_in_file(f, path) !=3:
                raise FileIsNotCorrect("sum_in_files: файл "+ f +" должен содержать ровно три строки")

        s = 0
        for f in [file1, file2]:
            with open(path + f, "rt") as file:
                for line in file:
                    try:
                        s += int(line.rstrip())
                    except ValueError as e:
                        print("sum_in_files: Ошибка: строка \"" + line + "\" файла " + file1 +" не может быть преобразована в число")
                        logging.exception(e)
                        return None
        logging.debug(f"sum_in_files: суммирование прошло успешно, итоговое значение {s}")                          
        return s

    except FileIsNotCorrect as e:
        print(e)
        logging.exception(e)
    except FileNotFoundError as e:
        print("sum_in_files: неверно указан путь или введенное число не соответствует имени файла")
        logging.exception(e)


def main():

    try:
        path = "./Files_work_container/"
        if not os.path.exists(path):
            os.mkdir(path)

        for i in range(10):
            name = path + str(i+1) + ".txt"
            with open(name, "w") as f:
                for j in range(3):
                    f.write(str(randint(-100,100)) + "\n")
        
        n1 = randint(1,10)
        n2 = randint(1,10)
        
        print(sum_in_files(n1, n2, path))

    except FileNotFoundError as e:
        print("main: неверно указан путь или введенное число не соответствует имени файла")
        logging.exception(e)



if __name__ == "__main__":
    main()