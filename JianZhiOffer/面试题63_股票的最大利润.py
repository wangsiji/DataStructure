# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 7:42 下午
# @Author  : siJi
# @File    : 面试题63_股票的最大利润.py
# @Desc    :

"""
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:
输入: [7,1,5,3,6,4] 输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1] 输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 
限制：0 <= 数组长度 <= 10^5
"""

"""
状态方程：
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
    dp[i][1] = max(dp[i-1][1], -prices[i])
    0<=i<=n-1
base case:
    dp[-1][0] = 0
    dp[-1][1] = -infinity
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 1)]
        dp[0][1] = float("-inf")
        for i in range(len(prices)):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + prices[i])
            dp[i + 1][1] = max(dp[i][1], -prices[i])
        return dp[-1][0]


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
