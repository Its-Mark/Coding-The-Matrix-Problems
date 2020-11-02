def my_filter(L, num):
    for i in range(L.count(num)):
        L.remove(num)

    print(L)


def my_lists(L):
    newList = []
    for i in range(len(L)):
        temp = []
        for j in range(L[i]):
            temp.append(j + 1)
        newList.append(temp)

    print(newList)


def my_function_composition(f, g):
    return 0




x = [1, 2, 4]

my_lists(x)
