def palindrom(string1: str) -> bool:

    if len(string1) == 1 or len(string1) == 0:
        return True

    count = 0
    length = len(string1)
    return palicheck(string1, count, length)


def palicheck(string1, count, length):

    if string1[count] != string1[length-count-1]:
        return False

    if length == (count + 1) * 2 or length == (count + 1) * 2 + 1:
        return True

    return palicheck(string1, count + 1, length)
