def string_in_string(list1, list2):
    leng1 = len(list1)
    leng2 = len(list2)

    for i in range(leng1-leng2+1):
        for j in range(leng2):
            if list[i+j]!= list2[j]:
                break
            if j == leng2-1:
                return True
    return leng2 == 0

print(string_in_string("133", ""))
