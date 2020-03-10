# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 11:10 下午
# @Author  : siJi
# @File    : 面试题10_II_青蛙跳台阶问题.py
# @Desc    : 动态规划


"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2 输出：2

示例 2：
输入：n = 7 输出：21

提示：0 <= n <= 100
"""

"""
dp[i] = dp[i-1] + dp[i-2]

dp[0] = 0 
dp[1] = 1 
dp[2] = 2
"""


class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''方法一'''
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # dp = [0 for _ in range(n + 1)]
        # dp[1], dp[2] = 1, 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[-1] % 1000000007
        '''方法二'''
        a, b = 1, 2
        for _ in range(1, n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == "__main__":
    print(Solution().numWays(7))
