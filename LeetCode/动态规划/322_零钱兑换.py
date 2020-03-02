# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 5:05 下午
# @Author  : siJi
# @File    : 322_零钱兑换.py
# @Desc    : 动态规划


"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1

说明:
你可以认为每种硬币的数量是无限的。
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        if len(coins) == 1 and coins[0] > amount:
            return -1
        dp = [-1 for _ in range(amount + 1)]  # 建立存储空间并初始化
        dp[0] = 0
        for i in range(1, amount + 1):
            cur_min = amount + 1
            for c in coins:
                # 当钱币面值小于当前需要凑的金额时
                if c <= i:
                    cur_min = dp[i - c] if dp[i - c] < cur_min else cur_min
            dp[i] = cur_min + 1 if cur_min < amount + 1 else amount + 1
        if dp[-1] == amount + 1:
            return -1
        else:
            return dp[-1]



if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))
