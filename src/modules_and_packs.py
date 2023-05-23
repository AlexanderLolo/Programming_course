# from Testpacks.Package1 import f_min 
from Testpacks.Package2 import f_palindrom 

print("введите три целых числа")
n = int(input("введите первое число"))
m = int(input("введите второе число"))
k = int(input("введите третье число"))

if f_palindrom.minpalicheck(n, m, k):
    print("минимальное число является палиндромом")
else:
    print("минимальное число не является палиндромом")