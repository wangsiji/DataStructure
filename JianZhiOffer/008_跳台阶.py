# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 10:58 下午
# @Author  : siJi
# @File    : 008_跳台阶.py
# @Desc    : 递归


"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        """动态规划 1 """
        # if number == 1:
        #     return 1
        # if number == 2:
        #     return 2
        # dp = [0] * (number + 1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, number+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[-1]
        """动态规划 2 """
        first = 1
        second = 1
        for i in range(number):
            first, second = second, first + second
        return first


if __name__ == "__main__":
    print(Solution().jumpFloor(6))
