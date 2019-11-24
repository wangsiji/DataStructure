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


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums
        cur_sum = 0  # 当前最大连续子序列和
        res = nums[0]  # 结果
        for i in range(len(nums)):
            # 如果 cur_sum > 0，则说明 cur_sum 对结果有增益效果，则 cur_sum 保留并加上当前遍历数字
            if cur_sum > 0:
                cur_sum += nums[i]
            # 如果 cur_sum <= 0，则说明 cur_sum 对结果无增益效果，需要舍弃，则 cur_sum 直接更新为当前遍历数字
            else:
                cur_sum = nums[i]
            res = max(cur_sum, res)
        return res


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
