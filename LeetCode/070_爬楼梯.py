# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 9:44 上午
# @Author  : siJi
# @File    : 070_爬楼梯.py
# @Desc    : 动态规划


"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""

"""
状态方程： 
    dp[i] = dp[i-1] + dp[i-2]
    0 <= i <= n-1
base case: 
    dp[-1]=dp[-2] = 0
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """动态规划，时间复杂度：O(n), 空间复杂度：O(n)"""
        # if n == 1:
        #     return 1
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]
        """斐波那契数"""
        # if n == 1:
        #     return 1
        # first = 1
        # second = 2
        # for i in range(3, n+1):
        #     first, second = second, first + second
        #     print(first, second)
        # return second

        '''O(n)'''
        dp = [0 for _ in range(n + 2)]
        for i in range(n):
            dp[i + 1] = dp[i] + dp[i - 1]
        print(dp)


if __name__ == "__main__":
    print(Solution().climbStairs(4))
