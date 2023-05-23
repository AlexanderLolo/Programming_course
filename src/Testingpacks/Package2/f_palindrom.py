from Testingpacks.Package1 import f_min

def palindrom(num):
    n = num
    rev = 0
    while n != 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10
    return num == rev

def minpalicheck(n, m, k):
    c = f_min.min3(n, m, k)
    return palindrom(c)
