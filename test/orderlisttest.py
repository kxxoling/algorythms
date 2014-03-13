# This Python file uses the following encoding: utf-8
from orderlist import *

TEST_TIMES = 10


def create_random_list():
    return [1, 6, 7, 3, 8, 9]


def sort(unsorted_list):
    return unsorted_list.sort()


if __name__ == '__main__':
    lis = [create_random_list() for i in range(TEST_TIMES)]
    for li in lis:
        if bubble_sort(li) != sorted(li):
            print '冒泡排序出错！原始列表：%s；排序后的列表：%s。' % (li, bubble_sort(li))
        if insert_sort(li) != sorted(li):
            print '插入排序出错！原始列表：%s；排序后的列表：%s。' % (li, insert_sort(li))
        if select_sort(li) != sorted(li):
            print '选择排序出错！原始列表：%s；排序后的列表：%s。' % (li, select_sort(li))
        if fast_sort(li) != sorted(li):
            print '快速排序出错！原始列表：%s；排序后的列表：%s。' % (li, fast_sort(li))