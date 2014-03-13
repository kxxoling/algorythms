# This Python file uses the following encoding: utf-8


def bubble_sort(unsorted_list):
    lis = unsorted_list[:]
    for i in range(len(lis)):
        for j in range(i):
            if lis[i] < lis[j]:
                lis[i], lis[j] = lis[j], lis[i]
    return lis


def insert_sort(unsorted_list):
    """For better understanding, it could be writen like this:
    lis = unsorted_list
    temp = [lis[-1]]
    def insert_from_behind(li, i):
        for j in range(len(li)):
            if li[j] >= i:
                li.insert(j, i)
                break
            elif j == len(li)-1:
                li.append(i)


    for i in lis[:-1]:
        insert_from_behind(temp, i)
    """
    lis = unsorted_list[:]
    temp = [lis[-1]]
    for i in lis[:-1]:
        for j in range(len(temp)):
            if temp[j] >= i:
                temp.insert(j, i)
                break
            elif j == len(temp)-1:
                temp.append(i)

    return temp


def select_sort(unsorted_list):
    lis = unsorted_list[:]
    for i in range(len(lis), -1, -1):
        for j in range(i):
            if lis[j] > lis[i-1]:  # i-1
                lis[j], lis[i-1] = lis[i-1], lis[j]
    return lis


def fast_sort(unsorted_list):
    lis = unsorted_list[:]
    i, j, k = 0, len(lis)-1, lis[0]
    while i < j:
        for m in range(j, -1, -1):
            if lis[m] < lis[j]:
                lis[j], lis[i] = lis[i], lis[j]
                j -= 1
                break
            else:
                j -= 1
        for n in range(i, len(lis)):
            if lis[n] > lis[i]:
                lis[j], lis[i] = lis[i], lis[j]
                i += 1
                break
            else:
                i += 1
    return lis