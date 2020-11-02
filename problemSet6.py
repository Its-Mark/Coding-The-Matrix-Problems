def my_filter(L, num):
    for x in L:
        print(x)
        if (x % num == 0):
            L.pop(x)
        #if (temp % num == 0):
            #L.pop(temp)

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


my_filter([1, 2, 4, 5, 7], 2)

my_lists([0, 3])
my_lists([1, 2, 4])
