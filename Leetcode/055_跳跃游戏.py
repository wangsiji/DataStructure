# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 9:14 下午
# @Author  : siJi
# @File    : 055_跳跃游戏.py
# @Desc    :


"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。\
"""
"""
这是一个动态规划问题，通常解决并理解一个动态规划问题需要以下 4 个步骤：
    利用递归回溯解决问题
    利用记忆表优化（自顶向下的动态规划）
    移除递归的部分（自底向上的动态规划）
    使用技巧减少时间和空间复杂度
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        方法 1：回溯
            这是一个低效的解决方法。我们模拟从第一个位置跳到最后位置的所有方案。
            从第一个位置开始，模拟所有可以跳到的位置，然后从当前位置重复上述操作，当没有办法继续跳的时候，就回溯
        '''

        # def helper(position, nums):
        #     if position == len(nums) - 1: return True
        #     furthest_jump = min(position + nums[position], len(nums) - 1)
        #     for next_position in range(position + 1, furthest_jump + 1):
        #         if helper(next_position, nums):
        #             return True
        #     return False
        # return helper(0, nums)

        '''
        方法 2：自顶向下的动态规划
        自顶向下的动态规划可以理解成回溯法的一种优化。我们发现当一个坐标已经被确定为好 / 坏之后，结果就不会改变了，这意味着我们可以记录这个结果，每次不用重新计算。
            1.初始化 memo 的所有元素为 UNKNOWN，除了最后一个显然是 GOOD （自己一定可以跳到自己）
            2. 优化递归算法，每步回溯前先检查这个位置是否计算过（当前值为：GOOD / BAD）
                1. 如果已知直接返回结果 True / False
                2. 否则按照之前的回溯步骤计算
            3. 计算完毕后，将结果存入memo表中   
        '''
        # dp = ["U" for _ in range(len(nums))]
        # dp[-1] = "G"
        # def helper(position, nums):
        #     if dp[position] != "U":
        #         return True if dp[position] == "G" else False
        #     furthest_jump = min(position + nums[position], len(nums) - 1)
        #     for next_position in range(position + 1, furthest_jump + 1):
        #         if helper(next_position, nums):
        #             dp[next_position] = "G"
        #             return True
        #     dp[position] = "B"
        #     return False
        # return helper(0, nums)

        '''
        方法 3：自底向上的动态规划
        自底向上和自顶向下动态规划的区别就是消除了回溯。
        在实际使用中，自底向下的方法有更好的时间效率因为我们不再需要栈空间，可以节省很多缓存开销。
        更重要的事，这可以让之后更有优化的空间。回溯通常是通过反转动态规划的步骤来实现的。
        '''
        # dp = ["U" for _ in range(len(nums))]
        # dp[-1] = "G"
        # for i in range(len(nums) - 2, -1, -1):
        #     furthest_jump = min(i + nums[i], len(nums) - 1)
        #     for j in range(i+1, furthest_jump+1):
        #         if dp[j] == "G":
        #             dp[i] = "G"
        #             break
        # return dp[0] == "G"

        '''
        贪心算法
        '''
        last_pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(Solution().canJump(nums))
