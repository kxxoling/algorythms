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


# def fast_sort(unsorted_list, left, right):
#     left = left or 0
#     right = right or len(unsorted_list)-1
#
#     def adjust_array(li, left, right):
#         m = li[left]
#         while left < right:
#             while left < right and li[right] >= m:
#                 right -= 1
#             li[left] = li[right]
#             while left < right and li[left] <= m:
#                 left += 1
#             li[right] = li[left]
#         li[left] = m
#         return left
#
#     if left < right:
#         middle = adjust_array(unsorted_list, left, right)
#         fast_sort(unsorted_list, left, middle-1)
#         fast_sort(unsorted_list, middle+1, right)
#     else:
#         return unsorted_list
#
#
# def quick_sort(unsorted_list):
#     lis = unsorted_list[:]
#     return fast_sort(lis, 0, len(unsorted_list)-1)
def quick_sort(arr, left, right):
    key = arr[right]
    lp = left
    rp = right
    if lp == rp:
        return
    while True:
        while (arr[lp] <= key) and (rp > lp):
            lp += 1
        while (arr[rp] >= key) and (rp > lp):
            rp -= 1
        arr[lp], arr[rp] = arr[rp], arr[lp]
        if lp >= rp:
            break
    arr[rp], arr[right] = arr[right], arr[rp]
    if left < lp:
        quick_sort(arr, left, lp-1)
    quick_sort(arr, rp, right)
