# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 8:38 下午
# @Author  : siJi
# @File    : 188_买卖股票的最佳时机IV.py
# @Desc    :

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [2,4,1], k = 2 输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2:
输入: [3,2,6,5,0,3], k = 2 输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        import numpy as np
        if k > len(prices) / 2:
            dp = np.zeros((len(prices) + 1, 2))
            dp[0, 1] = float("-inf")
            for i in range(len(prices)):
                dp[i + 1, 0] = max(dp[i, 0], dp[i, 1] + prices[i])
                dp[i + 1, 1] = max(dp[i, 1], dp[i, 0] - prices[i])
            return int(dp[len(prices), 0])
        else:
            dp = np.zeros((len(prices) + 1, k + 1, 2))
            dp[0, :, 1], dp[:, 0, 1] = float("-inf"), float("-inf")
            for i in range(len(prices)):
                for j in range(1, k + 1):
                    dp[i + 1, j, 0] = max(dp[i, j, 0], dp[i, j, 1] + prices[i])
                    dp[i + 1, j, 1] = max(dp[i, j, 1], dp[i, j - 1, 0] - prices[i])
            return int(dp[len(prices), k, 0])


if __name__ == "__main__":
    prices = [3, 2, 6, 5, 0, 3]
    k = 10
    print(Solution().maxProfit(k, prices))
