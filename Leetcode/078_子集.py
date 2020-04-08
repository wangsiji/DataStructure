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


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        方法一 迭代
            开始假设输出子集为空，每一步都向子集添加新的整数，并生成新的子集。
        '''
        # output = [[]]
        # for num in nums:
        #     output += [curr + [num] for curr in output]
        #     print(output)
        # return output
        '''
        方法二 库函数
        '''
        # import itertools
        # res = []
        # for i in range(len(nums)+1):
        #     for tmp in itertools.combinations(nums, i):
        #         res.append(list(tmp))
        # return res
        '''
        方法三 回溯算法
        回溯法是一种探索所有潜在可能性找到解决方案的算法
        其实回溯算法关键在于:不合适就退回上一步
        
        算法:
        定义一个回溯方法 backtrack(first, curr)，第一个参数为索引 first，第二个参数为当前子集 curr。
            如果当前子集构造完成，将它添加到输出集合中。
            否则，从 first 到 n 遍历索引 i。
                将整数 nums[i] 添加到当前子集 curr。
                继续向子集中添加整数：backtrack(i + 1, curr)。
                从 curr 中删除 nums[i] 进行回溯。
        '''
        res = []

        def backtrack(nums, tmp):
            res.append(tmp)
            print(res)
            for i in range(len(nums)):
                backtrack(nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
