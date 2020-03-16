# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 3:15 下午
# @Author  : siJi
# @File    : 053_最大子序和.py
# @Desc    : 动态规划


"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""

"""
状态方程：
    dp[i] = max(dp[i-1]+nums[i], nums[i]])
    0<=i<=n-1
base case: 
    dp[-1] = -infinity
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''空间复杂度O(n)'''
        if len(nums) < 2:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

        '''空间复杂度O(1)'''
        # ans = nums[0]
        # res = 0  # 当前
        # for i in range(len(nums)):
        #     res = max(nums[i], res + nums[i])
        #     ans = max(res, ans)
        # return ans


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
