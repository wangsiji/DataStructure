# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:42 下午
# @Author  : siJi
# @File    : 039_组合总和.py
# @Desc    : 回溯算法 + 剪枝


"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。 解集不能包含重复的组合。

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        '''
        候选数组里有 2 ，如果找到了 7 - 2 = 5 的所有组合，再在之前加上 2 ，就是 7 的所有组合；
        同理考虑 3，如果找到了 7 - 3 = 4 的所有组合，再在之前加上 3 ，就是 7 的所有组合，依次这样找下去；
        '''
        res = []
        if not candidates: return res
        if min(candidates) > target: return res
        candidates.sort()

        def backtrack(candidates, target, tmp):
            if target == 0: res.append(tmp)
            if target < 0: return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                backtrack(candidates[i:], target - candidates[i], tmp + [candidates[i]])

        backtrack(candidates, target, [])
        return res


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
