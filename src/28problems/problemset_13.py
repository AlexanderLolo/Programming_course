def UFO(N: int, data: list, octal: bool) -> list:

    if octal:
        return [int(str(x), 8) for x in data]
    return [int(str(x), 16) for x in data]
