# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 7:39 下午
# @Author  : siJi
# @File    : 287_寻找重复数.py
# @Desc    : 数组


"""
给定一个包含 n + 1个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2] 输出: 2

示例 2:
输入: [3,1,3,4,2] 输出: 3

说明：
不能更改原数组（假设数组是只读的）。只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。数组中只有一个重复的数字，但它可能不止重复出现一次。
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''排序 时间：O(nlogn) 空间：O(1)'''
        # nums = sorted(nums)
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         return nums[i]
        '''集合'''
        # lookup = {}
        # for num in nums:
        #     lookup[num] = lookup.get(num, 0) + 1
        # for k, v in lookup.items():
        #     if v > 1:
        #         return k
        '''python'''
        # from collections import Counter
        # counter = Counter(nums)
        # return max(counter.keys(), key=counter.get)

        '''数组'''
        for i in range(len(nums)):
            while (i + 1) != nums[i]:
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(nums))
