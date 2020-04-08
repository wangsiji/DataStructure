# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 8:39 下午
# @Author  : siJi
# @File    : 309_最佳买卖股票时机含冷冻期.py
# @Desc    :

"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

示例:
输入: [1,2,3,0,2] 输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""

"""
每次 sell 之后要等一天才能继续交易
状态方程：
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
    dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])  # 第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
    0<=i<=n-1 
base case: 
    dp[-1][0] = 0 
    dp[-1][1] = -infinity
    dp[-2][0] = 0
    dp[-2][1] = -infinity
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 2)]
        dp[0][0], dp[0][1], dp[1][0], dp[1][1] = 0, float("-inf"), 0, float("-inf")
        for i in range(len(prices)):
            dp[i + 2][0] = max(dp[i + 1][0], dp[i + 1][1] + prices[i])
            dp[i + 2][1] = max(dp[i + 1][1], dp[i][0] - prices[i])
        return dp[len(prices) + 1][0]


if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]
    print(Solution().maxProfit(prices))
