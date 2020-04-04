# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 1:30 下午
# @Author  : siJi
# @File    : 136_只出现一次的数字.py
# @Desc    : 哈希表、数学、位运算


"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1] 输出: 1

示例 2:
输入: [4,1,2,1,2] 输出: 4
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        方法一 哈希表
        """
        # lookup = {}
        # for num in nums:
        #     lookup[num] = lookup.get(num, 0) + 1
        # for key, value in lookup.items():
        #     if value == 1:
        #         return key
        """
        方法二 数学
        2 * (a + b + c) - (a + a + b + b + c) = c
        """
        # return 2 * sum(set(nums)) - sum(nums)
        """
        方法三 位运算
        ^ :  异或, 相同为 0 ,相异为 1
        a ^ a = 0
        a ^ a ^ b = b
        """
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(nums))
