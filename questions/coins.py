#! /usr/bin/ebv python
# encoding: utf8


def get_all_combinations():
    """Q: 有足够量的1分、2分、5分硬币，请问凑齐1元钱有多少种方法？
    """
    s = 0
    for one in range(100):
        for two in range(50):
            for five in range(20):
                if one + two*2 + five*5 == 100:
                    print "一分%s枚，两分%s枚，五分%s枚" % (one, two, five)
                    s += 1
    return s


if __name__ == '__main__':
    print '共有%s种解法' % (get_all_combinations())