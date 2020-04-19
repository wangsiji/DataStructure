# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 11:47 上午
# @Author  : siJi
# @File    : 128_最长连续序列.py
# @Desc    :

"""
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        方法一 暴力
        时间复杂度：O(n*3)
        空间复杂度：O(1)
        '''
        # longest_streak = 0
        # for num in nums:
        #     current_steak = 1
        #     while num + 1 in nums:
        #         num += 1
        #         current_steak += 1
        #     longest_streak = max(longest_streak, current_steak)
        # return longest_streak
        '''
        方法二 排序
        时间复杂度：O(nlongn)
        空间复杂度：O(1)
        '''
        # if not nums:
        #     return 0
        #
        # nums.sort()
        #
        # longest_streak = 1
        # current_streak = 1
        #
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         if nums[i] == nums[i - 1] + 1:
        #             current_streak += 1
        #         else:
        #             longest_streak = max(longest_streak, current_streak)
        #             current_streak = 1
        #
        # return max(longest_streak, current_streak)
        '''
        方法 3：哈希表和线性空间的构造
        '''
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak



if __name__ == "__main__":
    nums = [1,2,0,1]
    print(Solution().longestConsecutive(nums))
