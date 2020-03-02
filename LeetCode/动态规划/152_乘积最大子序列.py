# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 11:46 上午
# @Author  : siJi
# @File    : 152_乘积最大子序列.py
# @Desc    :


"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:
输入: [2,3,-2,4] 输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1] 输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""

"""
状态转移方程：
    有两个状态：当前序列最大和当前序列最小(负数)
    dp[i][0] = min(dp[i-1][0] * nums[i], nums[i], dp[i][1] * nums[i]) # 指的是以第 i 个数结尾的 乘积最小的连续子序列
    dp[i][1] = max(dp[i-1][1] * nums[i], nums[i], dp[i][0] * nums[i]) # 指的是以第 i 个数结尾的 乘积最大的连续子序列
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0]
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        dp[0][0], dp[0][1] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = min(dp[i - 1][0] * nums[i], nums[i], dp[i - 1][1] * nums[i])
            dp[i][1] = max(dp[i - 1][1] * nums[i], nums[i], dp[i - 1][0] * nums[i])
        return max([i[1] for i in dp])


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(Solution().maxProduct(nums))
