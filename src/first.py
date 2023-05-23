def num_digit(n):
    
    count = 1 #не делаю проверки на правильность введения параметра    
    while n // 10 != 0:
        n = n // 10
        count += 1
        
    return count
    
n1 = int(input("введите первое число"))
n2 = int(input("введите второе число"))

if num_digit(n1) > num_digit(n2):
    print("в первом больше")
elif num_digit(n1) < num_digit(n2):
    print("во втором больше")
else:
    print("equal")
