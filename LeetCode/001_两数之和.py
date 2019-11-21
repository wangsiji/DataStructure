# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 8:49 下午
# @Author  : siJi
# @File    : 01_两数之和.py
# @Desc    : 数组、哈希表

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9 所以返回 [0, 1]
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = dict()
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in lookup:
                return [lookup[tmp], i]
            else:
                lookup[nums[i]] = i


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 11]
    target = 12
    print(Solution().twoSum(nums, target))
