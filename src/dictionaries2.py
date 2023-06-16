import random

def second_excersise_funct(list, n):

    dict ={}
    for i in range(len(list)):

        if list[i] in dict.keys():
            dict[list[i]] += 1
        else:
            dict[list[i]] = 1

    b =[]

    for key, value in dict.items():
        if value >= n:
            b.append(key)

    # for key in dict.keys():
    #     print(key, dict.get(key))
    print(b)
    return b
 

def main():
    
    list = []
    for i in range(100):
        list.append(random.randint(1,10))

    # print(list)
    second_excersise_funct(list, 10)


if __name__ == "__main__":
    main()