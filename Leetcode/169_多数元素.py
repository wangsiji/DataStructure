# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 2:33 下午
# @Author  : siJi
# @File    : 169_多数元素.py
# @Desc    : 摩尔投票

"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3] 输出: 3

示例 2:
输入: [2,2,1,1,1,2,2] 输出: 2
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            if res == 0:
                x = num
            res  += 1 if num == x else -1
        return x

if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(Solution().majorityElement(nums))