# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:53 下午
# @Author  : siJi
# @File    : 090_子集II.py
# @Desc    :


"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        def backtrack(nums, tmp):
            if tmp not in res:
                res.append(tmp)
            for i in range(len(nums)):
                backtrack(nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


if __name__ == "__main__":
    nums = [4,4,4,1,4]
    print(Solution().subsetsWithDup(nums))
