# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 12:56 下午
# @Author  : siJi
# @File    : 面试题56_I_数组中数字出现的次数.py
# @Desc    :

"""

一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
输入：nums = [4,1,4,6] 输出：[1,6] 或 [6,1]

示例 2：
输入：nums = [1,2,10,4,1,4,3,3] 输出：[2,10] 或 [10,2]
 
限制：2 <= nums <= 10000
"""


class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        计算机中 数字都是以补码形式存在，正数补码等于自己，负数的补码等于反码+1
        
        由于异或的性质是，同一位相同则为 0，不同则为 1. 我们将所有数字异或的结果一定不是 0，也就是说至少有一位是 1.
        就是你取的那一位是 0 分成 1 组，那一位是 1 的分成一组。
        '''

        ret = 0  # 所有数字异或的结果
        a = 0
        b = 0
        for n in nums:
            ret ^= n
        # 找到第一位不是0的 左移
        h = 1
        while ret & h == 0:
            h <<= 1
        for n in nums:
            # 根据该位是否为0将其分为两组
            if h & n == 0:
                a ^= n
            else:
                b ^= n

        return [a, b]

if __name__ == "__main__":
    nums = [1,2,5,2]
    print(Solution().singleNumbers(nums))