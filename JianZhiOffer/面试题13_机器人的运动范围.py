# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 5:11 下午
# @Author  : siJi
# @File    : 面试题13_机器人的运动范围.py
# @Desc    :
# TODO
"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？


示例 1：
输入：m = 2, n = 3, k = 1 输出：3

示例 1：
输入：m = 3, n = 1, k = 0 输出：1

提示：
1 <= n,m <= 100 0 <= k <= 20
"""


def sums(x):
    s = 0
    while x:
        s += x % 10
        x = x // 10
    return s


class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(m):
            for j in range(n):
                if i + j <= k:
                    count += 1
                    print(i, j)
        return count


if __name__ == "__main__":
    m = 11
    n = 8
    k = 16
    print(Solution().movingCount(m, n, k))
    print(sums(1111))
