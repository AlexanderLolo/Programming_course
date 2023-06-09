import os.path

def Dirdelete(path):

    if not os.path.isdir(path):
        print("каталог не существует")
        return False
        
    else:
        try:
            for root, dirs, files in os.walk(path):

                if len(dirs) != 0:
                    return False

                for i in files:
                    os.remove(root+i) 

            os.rmdir(path)            
            
            if not os.path.isdir(path): # на всякий случай проверяю, существует ли еще каталог. Возможно каталог не удалился, но и исключение не было вызвано
                return True
            return False
        
        except Exception as e: # сложно сказать, когда возникнет исключение, а когда команда по чтению/удалению просто не выполниться, поэтому помещаю тело всей функции в блок          
            return False

  
def main():
    path = "./Test_dir2/"
    print(Dirdelete(path))
     
if __name__ == "__main__":
    main()

