def TheRabbitsFoot(str1: str, encode: bool) -> str:

    string1 = str1.rstrip().replace(" ", "")

    if len(string1) == 0:
        return ""

    leng = len(string1)
    leng_sqrt = int(leng ** (1/2))

    if leng_sqrt ** 2 == leng:
        n_rows = leng_sqrt
        n_colomns = leng_sqrt

    elif leng_sqrt * (leng_sqrt + 1) >= leng:
        n_rows = leng_sqrt
        n_colomns = leng_sqrt + 1
    else:
        n_rows = leng_sqrt + 1
        n_colomns = leng_sqrt + 1

    if encode:
        return Encrypt(string1, n_colomns)
    return Decrypt(string1, n_colomns, n_rows)


def Encrypt(string1: str, n_colomns):

    encrypted = ""
    for i in range(n_colomns):
        encrypted += string1[i::n_colomns]
        if i != n_colomns-1:
            encrypted += " "
    return encrypted

def Decrypt(string1: str, n_colomns: int, n_rows: int):

    decrypted = ""
    tail = ""

    if len(string1) == n_rows * n_colomns:
        number_of_let = 0
        n_rows += 1
    else:
        number_of_let = n_colomns - (n_rows * n_colomns-len(string1))

    for i in range(number_of_let, 0, -1):
        tail = string1[n_rows * i-1] + tail
        string1 = string1[:n_rows * i-1] + string1[n_rows * i:]

    for i in range(n_rows-1):
        decrypted += string1[i::n_rows-1]

    return decrypted + tail