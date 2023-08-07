import os


def file_gathering(path: str) -> list:

    if not os.path.isdir(path):
        print("каталог не существует")
        return -1

    return gathering(path)


def gathering(path: str) -> None:

    content = []

    for element in os.listdir(path):
        if os.path.isdir(os.path.join(path, element)):
            content.extend(gathering(os.path.join(path, element)))
        else:
            content.append(element)
    return content
