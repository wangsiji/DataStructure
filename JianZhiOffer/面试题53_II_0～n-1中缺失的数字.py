# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 3:16 下午
# @Author  : siJi
# @File    : 面试题53_II_0～n-1中缺失的数字.py
# @Desc    : 数学

"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3] 输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9] 输出: 8
 
限制：1 <= 数组长度 <= 10000
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        方法一 数学法
        [0, 1, 3] n=3
        [0, 1, 2, 3] (0+n)*(n+1)/2
        '''
        # return len(nums) * (len(nums) + 1) / 2 - sum(nums)
        '''
        方法一 二分查找
        一直二分找乱序的一侧
        '''
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    nums = [0,1,2,3,4,5,6,7,9]
    print(Solution().missingNumber(nums))
