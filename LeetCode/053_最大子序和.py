# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 9:08 上午
# @Author  : siJi
# @File    : 053_最大子序和.py
# @Desc    :


"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4], 输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        动态规划
        状态定义：dp[i] 以第 i 个数结尾的「连续子数组的最大和」，
        状态方程：dp[i] = max(dp[i - 1] + nums[i], nums[i]) 
        EX:
            nums [-2, 1, -3, 4, -1, 2, 1, -5, 4]
            dp   [-2, 1, -2, 4,  3, 5, 6,  1, 5]
        """
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        print(dp)
        pass


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
