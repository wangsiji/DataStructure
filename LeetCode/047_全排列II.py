# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:52 下午
# @Author  : siJi
# @File    : 047_全排列II.py
# @Desc    :

"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(nums, tmp):
            if not nums and tmp not in res:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
