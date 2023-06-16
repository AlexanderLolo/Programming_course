import random

def main():
    dict = {}
    i = 1

    while i <= 100:
        key = random.randint(1, 1000)
        if key in dict.keys():
            continue
        val = str(random.randint(1, 1000000))
        dict[key] = val
        i += 1

    for key in dict.keys():
        print(key, dict.get(key))

    dict.clear()

    # альтернативный поэлементный метод удаления
    # keyslist = []
    # for key in dict.keys():
    #     keyslist.append(key)

    # for i in range(len(dict)):
    #     del dict[keyslist[i]]


if __name__ == "__main__":
    main()