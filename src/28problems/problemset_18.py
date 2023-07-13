def MisterRobot(N: int, list1: list) -> bool:

    flag = True

    while flag:
        flag = False

        for i in range(N-2):
            if list1[i] > list1[i+1] and list1[i] >= list1[i+2]:
                list1[i],list1[i+2] = list1[i+2],list1[i]
                list1[i],list1[i+1] = list1[i+1],list1[i]
                flag = True

            if list1[i+1] > list1[i+2]:
                list1[i+1],list1[i+2] = list1[i+2],list1[i+1]
                list1[i+1],list1[i] = list1[i],list1[i+1]
                flag = True
    
    return list1[0] <= list1[1]


