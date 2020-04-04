# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:51 下午
# @Author  : siJi
# @File    : 046_全排列.py
# @Desc    :

"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        方法一 库函数
        '''
        # import itertools
        # return list(itertools.permutations(nums))

        '''
        方法二 回溯算法
        '''
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
