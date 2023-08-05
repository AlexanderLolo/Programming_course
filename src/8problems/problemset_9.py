def genparenthesis(N: int) -> list:

    content = []
    string = "("
    gathering(string, 1, N-1, content)
    print(content)
    return content


def gathering(string: str, balance: int, count: int, content: list) -> None:

    if count == 0 and balance == 0:
        content.append(string)

    if count > 0:
        gathering(string + "(", balance + 1, count - 1, content)

    if balance > 0:
        gathering(string + ")", balance - 1, count, content)


print(genparenthesis(3))
