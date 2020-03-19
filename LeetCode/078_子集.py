# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 5:15 下午
# @Author  : siJi
# @File    : 078_子集.py
# @Desc    : 递归、回溯、

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

"""
递归
回溯
基于二进制位掩码和对应位掩码之间的映射字典生成排列/组合/子集


"""
# TODO


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        方法一 递归
            开始假设输出子集为空，每一步都向子集添加新的整数，并生成新的子集。
        '''
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
