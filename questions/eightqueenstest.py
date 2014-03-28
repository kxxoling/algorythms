# !/usr/bin/python
# This Python file uses the following encoding: utf-8
import unittest
from questions.eight import *



class TestCase(unittest.TestCase):
    def setUp(self):
        self.lists = [create_random_list() for i in range(TEST_TIMES)]

    def test_bubble_sort(self):
        for lis in self.lists:
            li = lis
            assert bubble_sort(li) == sorted(lis)

    def test_insert_sort(self):
        for lis in self.lists:
            li = lis
            assert insert_sort(li) == sorted(lis)

    def test_select_sort(self):
        for lis in self.lists:
            li = lis
            assert select_sort(li) == sorted(lis)

    def test_quick_sort(self):
        for lis in self.lists:
            li = lis
            quick_sort(li, 0, ARRAY_LENGTH-1)
            assert li == sorted(lis)


if __name__ == '__main__':
    unittest.main()