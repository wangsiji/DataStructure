# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 10:15 下午
# @Author  : siJi
# @File    : 034_在排序数组中查找元素的第一个和最后一个位置.py
# @Desc    : 中等｜

"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。 如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8 输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6 输出: [-1,-1]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 左边界
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        low = -1 if left == 0 else left
        # 右边界
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        print(left, right)
        high = -1 if left == len(nums) else left - 1
        return [low, high]


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 6
    print(Solution().searchRange(nums, target))
