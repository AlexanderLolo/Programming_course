import os


def Filegathering(path: str) -> list:

    if not os.path.isdir(path):
        print("каталог не существует")
        return -1
    else:
        content = []
        return Gathering(path, content)


def Gathering(path: str, content: list) -> list:

    for element in os.listdir(path):
        if os.path.isdir(os.path.join(path, element)):
            Gathering(os.path.join(path, element), content)
        else:
            content.append(element)

    return content
