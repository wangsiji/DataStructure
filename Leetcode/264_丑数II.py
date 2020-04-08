# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 4:40 下午
# @Author  : siJi
# @File    : 264_丑数II.py
# @Desc    : 动态规划

"""
编写一个程序，找出第 n 个丑数。丑数就是只包含质因数 2, 3, 5 的正整数。

示例:
输入: n = 10 输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:  
1 是丑数。
n 不超过1690。
"""

"""
dp[i] = dp[i-1]*2, dp[i-1]*3, dp[i-1]*5
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        方法一 动态规划
        '''
        # dp = [0 for _ in range(n)]
        # dp[0] = 1
        # i2, i3, i5 = 0, 0, 0
        # for i in range(1, n):
        #     dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
        #     if dp[i] == dp[i2] * 2:
        #         i2 += 1
        #     if dp[i] == dp[i3] * 3:
        #         i3 += 1
        #     if dp[i] == dp[i5] * 5:
        #         i5 += 1
        # return dp[-1]
        '''
        方法二 最小堆
        '''
        import heapq
        heap = [1]
        heapq.heapify(heap)
        res = 0
        for _ in range(n):
            print(heap)
            res = heapq.heappop(heap)
            # 去除重复的
            while heap and res == heap[0]:
                res = heapq.heappop(heap)
            a, b, c = res * 2, res * 3, res * 5
            for t in [a, b, c]:
                heapq.heappush(heap, t)
        return res


if __name__ == "__main__":
    print(Solution().nthUglyNumber(10))
