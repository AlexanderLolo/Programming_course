def BigMinus(str1: str, str2: str) -> str:

    if len(str1) > len(str2):
        maxstr = str1
        minstr = str2

    elif len(str1) < len(str2):
        maxstr = str2
        minstr = str1

    else:
        maxstr = max(str2, str1)
        minstr = min(str2, str1)

    if str1 == str2:
        return "0"
    else:
        return MinusNumber(maxstr, minstr)


def MinusNumber(str1: str, str2: str) -> str:
    # Function returns string(number) minus string(number)
    # If strings are equal, function returns ""

    if str1 == str2:
        return ""
    if str2 == "":
        return str1
    else:
        b = MinusDigit(str1, str2[-1])
        return MinusNumber(b[:-1], str2[:-1]) + b[-1]


def MinusDigit(str1: str, digit: str) -> str:
    #  function returns string(number) minus string(one digit number)

    length = len(str1)

    if length == 2:
        return str(int(str1) - int(digit))
    elif str1[length-1] >= digit:
        return str1[:length-1] + str(int(str1[length-1]) - int(digit))
    else:
        return (MinusDigit(str1[:length-1], "1")
                + str(int(str1[length-1]) - int(digit) + 10))
