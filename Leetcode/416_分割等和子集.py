# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 7:54 上午
# @Author  : siJi
# @File    : 416_分割等和子集.py
# @Desc    :

"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        '''
        dp[i][j]表示在前i个物品（元素）选或者不选可以装满容量j的背包。
        
        dp[i][j] = dp[i-1][j]           # 装i
        dp[i][j] = dp[i-1][j-nums[i]    # 不装i
        
        
         '''
        n = len(nums)
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(1, target + 1):
            if nums[0] == i:
                dp[0][i] = True
                break
        for i in range(1, n):
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - nums[i]])
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[-1][-1]

        '''
        方法二 压缩空间
        '''
        # target, mod = divmod(sum(nums), 2)
        # if mod != 0:
        #     return False
        # dp = [False for _ in range(target + 1)]
        # dp[0] = True
        # for i in range(len(nums)):
        #     for j in range(target, nums[i] - 1, -1):
        #         dp[j] = dp[j] or dp[j - nums[i]]
        # return dp[-1]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(Solution().canPartition(nums))
