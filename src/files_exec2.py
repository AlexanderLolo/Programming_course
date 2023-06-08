import logging

logging.basicConfig(filename='./Files_work_container/files_exec2.log', level=logging.DEBUG, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

class Cat:
 
    def set_name(self, name):
        self.__name = name

    def set_speed(self, speed):
        self.__speed = speed

    def set_fq(self, fq):
        self.__fq = fq

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def get_fq(self):
        return self.__fq


def cats_obj(filename, path):

    cats_list = []

    try:
        name = path + filename
        with open(name, "rt") as file:
            for line in file:
                try:
                    list = line.split()
                    if len(list) != 3:
                        logging.debug(f"строка {line} некорректна и будет пропущена(должно быть ровно три слова)")                 
                    elif int(list[1]) < 0 or int(list[1]) > 60:
                        logging.debug(f"строка {line} некорректна. Параметр скорости выходит за рамки допустимого") 
                    elif int(list[2]) < 0 or int(list[2]) > 300 :
                        logging.debug(f"строка {line} некорректна. Параметр частоты мурлыканья выходит за рамки допустимого")
                    else:
                        cat = Cat()
                        cat.set_name(list[0])
                        cat.set_speed(list[1])
                        cat.set_fq(list[2])
                        cats_list.append(cat)
                        logging.debug(f"строка {line} корректна. Котик будет добавлен")

                except ValueError as e:
                    logging.debug("строка \"" + line + "\" содержит некорректные параметры для скорости и/или частоты мурлыканья")

    except FileNotFoundError as e:
        print("cats_obj: неверно указан путь или имя файла")
        logging.exception(e)

    return cats_list

def main():
    
    path = "./Files_work_container/"
    file_name = "cats.txt"

    a = cats_obj(file_name, path)

    print("длина списка - ", len(a))
    for i in range(len(a)):
        print(a[i].get_name(), a[i].get_speed(), a[i].get_fq())

if __name__ == "__main__":
    main()