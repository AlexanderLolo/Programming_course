from zipfile import ZipFile
import os

# функция сканирует только текущую директорию. Если архив уже существует, то она его перезаписывает
def arch_func(arch_name, ext):

    with ZipFile(arch_name, "w") as zippi:
    
        for file in os.listdir("./"):
            if os.path.isdir(file):
                continue
            
            elif (ext == ".*" or file.endswith(ext)) and file != arch_name: # если не добавить последнее условие, то возможен бесконечный цикл
                zippi.write(file)
                # print(os.path.abspath(file))

# функция сканирует текущую и все поддиректории и записывает файлы с указанным расширением
def arch_func1(arch_name, ext):

    with ZipFile(arch_name, "w") as zippi:

        for root, dirs, files in os.walk("./"):

            for i in files:
        
                if (ext == ".*" or i.endswith(ext)) and i != arch_name:
                    zippi.write(os.path.join(root, i))

# как понял из задания архив всегда создается новый, поэтому не реализовывал проверку, существуют ли в архиве уже добавлянмые файлы.
# такую проверку нетрудно реализовать с помощью метода namelist()

def main():

    name = "new_arch.zip"
    name1 = "new_arch1.zip"
    ext = ".*"

    arch_func(name, ".txt")
    arch_func1(name1, ".txt")

    # with ZipFile(name1) as zip:
    #     print(zip.namelist())

if __name__ == "__main__":
    main()