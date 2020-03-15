# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 6:09 下午
# @Author  : siJi
# @File    : 面试题61_扑克牌中的顺子.py
# @Desc    : 数组


"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:
输入: [1,2,3,4,5]
输出: True
 
示例 2:
输入: [0,0,1,2,5] 输出: True

限制： 数组长度为 5 数组的数取值为 [0, 13]
"""


class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        方法一 不排序方式
        如果我们能够知道 5 张扑克牌中的最大值 maxValue 和最小值 minValue ，那我们就知道，要使它为顺子需要 maxValue−minValue+1 张牌。
        '''
        # min_value = 14
        # max_value = 0
        # lookup = {}
        # for num in nums:
        #     # 去除大小王
        #     if num == 0:
        #         continue
        #     # 重复
        #     if num in lookup:
        #         return False
        #     else:
        #         lookup[num] = True
        #     min_value = min(min_value, num)
        #     max_value = max(max_value, num)
        # return max_value - min_value + 1 <= 5

        '''
        方法二 排序方式
            排序之后扑克牌就有序了，我们就可以直接判断相邻两张牌之间需要多少个大王或小王来填补。
            如果需要填补大小王的数量，大于已有大小王的数量，则返回 false .
            相反，如果需要填补大小王的数量，小于或等于已有大小王的数量，则返回 true
        '''
        nums = sorted(nums)
        zero = 0
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                zero += 1
                continue
            if nums[i] == nums[i + 1]:
                return False
            zero -= nums[i + 1] - nums[i] - 1
        return zero >= 0


if __name__ == "__main__":
    nums = [0, 2, 3, 4, 5]
    print(Solution().isStraight(nums))
