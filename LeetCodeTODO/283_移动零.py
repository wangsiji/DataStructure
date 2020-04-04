# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 7:02 下午
# @Author  : siJi
# @File    : 283_移动零.py
# @Desc    :

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12] 输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。尽量减少操作次数。
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''两次遍历'''
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[j] = nums[i]
        #         j += 1
        # for i in range(j, len(nums)):
        #     nums[i] = 0
        # return nums
        '''一次遍历'''
        # j = 0  # 慢指针
        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[j], nums[i] = nums[i], nums[j]
        #         j += 1
        # return nums

        '''一次遍历方法二'''
        i = j = 0
        while i < len(nums):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                i += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(nums))
