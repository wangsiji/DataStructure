# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 9:43 上午
# @Author  : siJi
# @File    : 581_最短无序连续子数组.py
# @Desc    : 双指针、排序

"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:
输入: [2, 6, 4, 8, 10, 9, 15] 输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

说明 :
输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。
"""


# TODO

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        方法一 双指针
        '''
        # # 左右边界
        # l, r = len(nums) - 1, 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] > nums[j]:
        #             l = min(i, l)
        #             r = max(j, r)
        # return 0 if l >= r else r - l + 1

        '''
        方法二 排序
        '''
        nums_sorted = sorted(nums)
        l, r = len(nums) - 1, 0
        for i in range(len(nums)):
            if nums[i] != nums_sorted[i]:
                l = min(l, i)
                r = max(r, i)
        return 0 if l >= r else r - l + 1


if __name__ == "__main__":
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(Solution().findUnsortedSubarray(nums))
