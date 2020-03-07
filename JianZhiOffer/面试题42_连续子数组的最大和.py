# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 7:07 下午
# @Author  : siJi
# @File    : 面试题42_连续子数组的最大和.py
# @Desc    :


"""
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。

示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4] 输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 
提示：1 <= arr.length <= 10^5 -100 <= arr[i] <= 100
"""

"""
状态方程：
    dp[i] = max(nums[i], dp[i-1]+nums[i])
base case:
    dp[-1] = 0
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        return max(dp)


if __name__ == "__main__":
    nums = [-2,-1]
    print(Solution().maxSubArray(nums))
