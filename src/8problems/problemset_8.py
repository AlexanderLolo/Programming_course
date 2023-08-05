import os


def file_gathering(path: str) -> list:

    if not os.path.isdir(path):
        print("каталог не существует")
        return -1

    content = []
    gathering(path, content)

    return content


def gathering(path: str, content: list) -> None:

    for element in os.listdir(path):
        if os.path.isdir(os.path.join(path, element)):
            gathering(os.path.join(path, element), content)
        else:
            content.append(element)
