# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 9:03 下午
# @Author  : siJi
# @File    : 面试题14_I_剪绳子.py
# @Desc    : 动态规划

"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。
请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：
输入: 2 输出: 1 解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10 输出: 36 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：2 <= n <= 58
"""
"""
状态数组dp[i]表示：数字 i 拆分为至少两个正整数之和的最大乘积

"""


class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        动态规划：
        状态数组dp[i]表示：数字 i 拆分为至少两个正整数之和的最大乘积。为了方便计算，dp 的长度是 n + 1，值初始化为 1。
        '''
        # dp = [1 for _ in range(n + 1)]
        # for i in range(3, n + 1):
        #     for j in range(1, i):
        #         dp[i] = max(dp[i], j * (i - j), dp[j] * (i - j))
        # return dp[-1]
        '''
        数学
        贪心法则：尽可能分解出多的3，3 的个数为 a，得到余数 b 可能为 0，1，2：

        b = 0，返回 3**a；
        b = 1，我们将末尾的的3+1分解成2×2，因此返回 3**(a-1)*4
        b = 2，返回 3**a * 2 
        '''
        import math
        if n < 4: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)



if __name__ == "__main__":
    print(Solution().cuttingRope(3))
