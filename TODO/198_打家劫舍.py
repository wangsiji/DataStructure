# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 5:12 下午
# @Author  : siJi
# @File    : 198_打家劫舍.py
# @Desc    : 动态规划


"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""

"""
f(k) = 从前 k 个房屋中能抢劫到的最大数额，Ai= 第 i 个房屋的钱数。
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """方法一"""
        # pre, cur = 0, 0
        # for num in nums:
        #     pre, cur = cur, max(cur, pre + num)
        # return cur

        """方法二"""
        # dp[n] = MAX( dp[n-1], dp[n-2] + num )
        dp = [0 for _ in range(len(nums) + 2)]
        for i in range(2, len(nums) + 2):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])
        return dp[-1]


if __name__ == "__main__":
    # nums = [2, 7, 9, 3, 1]
    nums = [1]
    print(Solution().rob(nums))
