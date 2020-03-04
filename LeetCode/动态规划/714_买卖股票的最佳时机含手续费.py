# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 8:41 下午
# @Author  : siJi
# @File    : 714_买卖股票的最佳时机含手续费.py
# @Desc    :

"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。

示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2 输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1 在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4 在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

注意: 0 < prices.length <= 50000. 0 < prices[i] < 50000. 0 <= fee < 50000.
"""
"""
状态方程：
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
    dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
base case:
    dp[-1][0] = 0
    dp[-1][1] = -infinity
"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        '''空间复杂度O(n)'''
        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 1)]
        dp[0][0], dp[0][1] = 0, float("-inf")
        for i in range(len(prices)):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + prices[i] - fee)
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - prices[i])
        return dp[len(prices)][0]
        # '''空间复杂度O(1)'''
        # cash, hold = 0, -prices[0]
        # for i in range(1, len(prices)):
        #     cash = max(cash, hold + prices[i] - fee)
        #     hold = max(hold, cash - prices[i])
        # return cash


if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(Solution().maxProfit(prices, fee))
