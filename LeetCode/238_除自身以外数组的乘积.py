# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 5:49 下午
# @Author  : siJi
# @File    : 238_除自身以外数组的乘积.py
# @Desc    : 数组

"""
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。


示例:
输入: [1,2,3,4] 输出: [24,12,8,6]

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        right = [1] * len(nums)
        for i in range(len(nums)-2,-1,  -1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(len(nums)):
            left[i] = left[i] * right[i]
        return left

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
