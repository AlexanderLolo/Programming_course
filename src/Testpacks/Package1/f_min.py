def min3(n1,n2,n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n3:
        return n2
    return n3
