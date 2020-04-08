# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 3:02 下午
# @Author  : siJi
# @File    : 034_在排序数组中查找元素的第一个和最后一个位置.py
# @Desc    :

"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        方法一 线性扫描
        '''
        # left_index, right_index = -1, -1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         left_index = i
        #         break
        # else:
        #     return [-1, -1]
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] == target:
        #         right_index = i
        #         break
        # return [left_index, right_index]

        '''
        方法二 二分查找
        '''
        # 第一次二分查找
        left , right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >=  target:
                right = mid
            else:
                left = mid + 1
        left_index = left
        if left_index == len(nums) and nums[left_index] != target:
            return [-1, -1]
        # 第二次二分查找
        left , right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <=  target:
                left = mid + 1
            else:
                right = mid
        return [left_index, right-1]

if __name__ == "__main__":
    nums = [1]
    target = 1
    print(Solution().searchRange(nums, target))
