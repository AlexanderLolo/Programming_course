from Testpacks.Package1 import f_min

def min3(n1,n2,n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n3:
        return n2
    return n3

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
