# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 10:17 下午
# @Author  : siJi
# @File    : 007_斐波拉契数列.py
# @Desc    : 递归


"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""


class Solution:
    def Fibonacci(self, n):
        # write code here
        """递归"""
        # if n < 2:
        #     return n
        # elif n == 2:
        #     return 1
        # else:
        #     return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
        """动态规划 1 """
        # if n < 2:
        #     return n
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # dp[2] = 1
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[-1]
        """动态规划 2 """
        if n < 2:
            return n
        first = 1
        second = 1
        for i in range(3, n + 1):
            first, second = second, first + second
        return second


if __name__ == "__main__":
    print(Solution().Fibonacci(0))
