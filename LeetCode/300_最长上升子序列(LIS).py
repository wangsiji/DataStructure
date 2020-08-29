# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 9:11 上午
# @Author  : siJi
# @File    : 300_最长上升子序列(LIS).py
# @Desc    :


"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18] 输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。 你算法的时间复杂度应该为 O(n2) 。
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        方法一 动态规划
        状态定义：dp[i] 表示以 nums[i] 结尾的「上升子序列」的长度
        状态方程：dp[i] = max(dp[j]+1) 0<=j<i
        EX:
            nums [10, 9, 2, 5, 3, 7, 101, 18]
            dp   [1, 1, 1, 2, 2, 3, 4, 4]
        """
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]> nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))
