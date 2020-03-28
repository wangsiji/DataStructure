# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 2:49 下午
# @Author  : siJi
# @File    : 面试题03_数组中重复的数字.py
# @Desc    : 哈希表


"""
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1： 输入： [2, 3, 1, 0, 2, 5, 3] 输出：2 或 3

限制：2 <= n <= 100000
"""


class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''方法一 排序 时间复杂度O(nlogn),空间复杂度O(1)'''
        # nums = sorted(nums)
        # res = nums[0]
        # for i in range(1, len(nums)):
        #     if res == nums[i]:
        #         return res
        #     res = nums[i]
        '''方法二 哈希表 时间复杂度O(n),空间复杂度O(n)'''
        # lookup = {}
        # for num in nums:
        #     if num not in lookup:
        #         lookup[num] = 0
        #     else:
        #         return num
        '''方法三 下标定位法 时间复杂度O(n),空间复杂度O(1)'''
        # 如果没有重复数字，那么正常排序后，数字i应该在下标为i的位置
        # 所以思路是重头扫描数组，遇到下标为i的数字如果不是i的话，（假设为m),那么我们就拿与下标m的数字交换。
        # 在交换过程中，如果有重复的数字发生，那么终止返回
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


if __name__ == "__main__":
    nums = [0, 1, 4, 3, 3]
    print(Solution().findRepeatNumber(nums))
