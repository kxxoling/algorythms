#! /usr/bin/ebv python
# encoding: utf8


def print_queens(queens):
    for queen in queens:
        row = ['x' for i in range(queen)]
        row.append('Q')
        row.extend(['x' for i in range(7-queen)])
        print ' '.join(row)
    print '-------------------'


def check(queens, num):
    if num == 0:
        return True
    for i in range(num):
        if queens[i] == queens[num]:
            return False
        elif abs(queens[i] - queens[num])/(num - i) == 1 and abs(queens[i] - queens[num]) % (num - i) == 0:
            return False
    return True


def check_queens(queens, num=0):
    if num >= 8:
        print_queens(queens)
    for i in range(8):
        try:
            queens[num] = i
        except IndexError:
            queens.append(i)
        if check(queens, num):
            check_queens(queens, num+1)


if __name__ == '__main__':
    check_queens([0,0,0,0,0,0,0,0])