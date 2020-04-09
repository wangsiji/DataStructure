# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 10:55 上午
# @Author  : siJi
# @File    : 494_目标和.py
# @Desc    :

"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
一共有5种方法让最终目标和为3。

注意:
数组非空，且长度不会超过20。
初始的数组的和不会超过1000。
保证返回的最终结果能被32位整数存下。
"""

# TODO
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        '''
        方法一 回溯
        '''
        # count = 0
        # res = []
        # n = len(nums)
        # def helper(nums, S, tmp):
        #     nonlocal count
        #     if S == 0 and len(tmp) == n:
        #         count += 1
        #         res.append(tmp)
        #         return
        #     for i in range(len(nums)):
        #         helper(nums[i + 1:], S + nums[i], tmp + [-nums[i]])
        #         helper(nums[i + 1:], S - nums[i], tmp + [+nums[i]])
        #     return count
        #
        # return helper(nums, S, [])
        '''
        方法二 枚举
        '''

        def helper(nums, i, sum, S):
            nonlocal count
            if i == len(nums) and sum == S:
                count += 1
            if i < len(nums):
                helper(nums, i + 1, sum + nums[i], S)
                helper(nums, i + 1, sum - nums[i], S)

        count = 0
        helper(nums, 0, 0, S)
        return count


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    S = 3
    print(Solution().findTargetSumWays(nums, S))
