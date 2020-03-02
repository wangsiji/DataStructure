# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 11:57 上午
# @Author  : siJi
# @File    : 121_ 买卖股票的最佳时机.py
# @Desc    :


"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4] 输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1] 输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

"""
0 <= i <= n-1, 1 <= k <= K,  0:未持有 1:持有
状态转移方程:
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
base case:
    dp[-1][k][0] = 0 
    dp[-1][k][1] = -infinity
    dp[i][0][0] = 0
    dp[i][0][1] = -infinity
"""

'''
当 k=1 时: 
状态方程:
    dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
                = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
    dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])
                = max(dp[i - 1][1][1], - prices[i])
                = max(dp[i - 1][1], - prices[i])
base case:
    dp[-1][0] = 0 
    dp[-1][1] = -infinity
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 1)]
        dp[0][0], dp[0][1] = 0, float("-inf")
        for i in range(len(prices)):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + prices[i])
            dp[i + 1][1] = max(dp[i][1], - prices[i])
        return dp[len(prices)][0]


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
