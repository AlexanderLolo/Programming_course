# программа корректно работает на Linux и некорректно на Windows
import os.path

def FileCheck(path, ext, flag):
    if not os.path.isdir(path):
        print("каталог не существует")
        return -1
    else:
        content = [[], []]
 
        for root, dirs, files in os.walk(path):

            if len(root.split("/")) > 3: # отсекаем папки второго уровня вложенности
                continue

            for j in dirs:
                content[0].append(j)
            
            for j in files:
                if j.split(".")[ len(j.split("."))-1 ] == ext:
                    content[1].append(j)

            if not flag:
                return content      
        return content

def main():
    path = "./Test_dir/"
    content = FileCheck(path, "txt", True)
 
    for j in range(len(content[0])):
        print(content[0][j])
            
    for j in range(len(content[1])):
        print(content[1][j])
    
if __name__ == "__main__":
    main()

