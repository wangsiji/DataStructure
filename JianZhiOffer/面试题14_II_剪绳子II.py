# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 4:15 下午
# @Author  : siJi
# @File    : 面试题14_II_剪绳子II.py
# @Desc    : 动态规划

"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。
请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入: 2 输出: 1 解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10 输出: 36 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：2 <= n <= 1000
"""


class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n + 1)]
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), dp[j] * (i - j))
        return dp[-1] % 1000000007


if __name__ == "__main__":
    n = 10
    print(Solution().cuttingRope(n))
