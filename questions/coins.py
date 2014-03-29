#! /usr/bin/ebv python
# encoding: utf8
"""Q: 有足够量的 1 分、2 分、5 分硬币，请问凑齐 1 元钱有多少种方法？
"""


def get_all_combinations():
    """这种情况下每种硬币出现的数量都是有限制的，考虑极限情况下，5 分硬币最多能够出现 100/5 次，
    2 分硬币最多出现 50 次，1分硬币最多出现 100次，因此有以下遍历算法。
    """
    s = 0
    for one in range(100):
        for two in range(50):
            for five in range(20):
                if one + two*2 + five*5 == 100:
                    print "一分%s枚，两分%s枚，五分%s枚" % (one, two, five)
                    s += 1
    return s


def get_all_combines():
    """在上面算法的基础上，我们发现 1 是 2、5、100 的公约数，因此只要 2 分、5 分硬币数量确定，剩下的可以使用 1 分填补，
    改进后的算法如下：
    """
    s = 0
    for two in range(50):
        for five in range(20):
            one = 100 - two*2 - five*5
            print "一分%s枚，两分%s枚，五分%s枚" % (one, two, five)
            s += 1
    return s


def get_all_cmbs():
    """再基于上面的想法，如果考虑到硬币数量确定的先后，5 分硬币数量决定后， 2 分硬币的极限会随之发生变化，算法改进后如下："""
    s = 0
    for five in range(20):
        for two in range((100-five*5)/2):
            one = 100 - two*2 - five*5
            print "一分%s枚，两分%s枚，五分%s枚" % (one, two, five)
            s += 1
    return s


if __name__ == '__main__':
    print '共有%s种解法' % (get_all_combinations())