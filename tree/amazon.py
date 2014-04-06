# !/usr/bin/python
# This Python file uses the following encoding: utf-8
"""It is said an Amazon review question is like this:
You are given a function calcDifference which takes in the root pointer of a binary tree as it’s input.
Complete the function to return the sum of values of nodes at odd height – sum of values of node at even height.
Consider the root node is at height 1. The structure is already declared, you can just start initializing nodes:
struct node {
struct node *left,*right;
int val;
}
This file is a Python solution for this question.
"""


class BiNode():
    def __init__(self, value, lchild, rchild):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class BiTree():
    sum = 0

    def __init__(self, root):
        self.root = root
        self.ltree = root.lchild and BiTree(root.lchild) or None
        self.rtree = root.rchild and BiTree(root.rchild) or None

    def cal_diff(self):
        """This method uses iterate to calculate
        the sum of values of nodes at odd height – sum of values of node at even height
        """
        self.sum += self.root.value
        if self.ltree:
            self.sum = self.sum - self.ltree.cal_diff()
        if self.rtree:
            self.sum -= self.rtree.cal_diff()
        return self.sum

if __name__ == '__main__':
    k = BiNode(3, None, None)
    j = BiNode(9, None, None)
    h = BiNode(5, None, None)
    g = BiNode(0, None, None)
    f = BiNode(8, None, None)
    d = BiNode(4, h, None)
    e = BiNode(7, j, k)
    b = BiNode(5, d, e)
    c = BiNode(6, f, g)
    a = BiNode(3, b, c)
    bt = BiTree(a)
    print bt.cal_diff()