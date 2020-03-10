# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 9:07 上午
# @Author  : siJi
# @File    : 面试题49_丑数.py
# @Desc    : 数学、动态规划

"""
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

示例:
输入: n = 10 输出: 12 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:  1 是丑数。n 不超过1690。
"""

"""

"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        方法一 堆
        '''
        # import heapq
        # heap = [1]
        # heapq.heapify(heap)
        # res = 0
        # for _ in range(n):
        #     res = heapq.heappop(heap)
        #     while heap and res == heap[0]:
        #         res = heapq.heappop(heap)
        #     for t in [res * 2 , res * 3, res * 5]:
        #         heapq.heappush(heap, t)
        # return res
        '''
        方法二 动态规划
        '''
        dp = [0 for _ in range(n)]
        dp[0] = 1
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            if dp[i] == dp[i2] * 2:
                i2 += 1
            if dp[i] == dp[i3] * 3:
                i3 += 1
            if dp[i] == dp[i5] * 5:
                i5 += 1
        return dp[-1]

if __name__ == "__main__":
    print(Solution().nthUglyNumber(10))
