def SumOfThe(N: int, data: list) -> int:

    for number in data:
        if sum(data) - number == number:
            return number
