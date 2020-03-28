# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 11:13 上午
# @Author  : siJi
# @File    : 面试题56_II_数组中数字出现的次数II.py
# @Desc    :


"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：
输入：nums = [3,4,3,3] 输出：4

示例 2：
输入：nums = [9,1,7,9,7,9,7] 输出：1
 
限制：
1 <= nums.length <= 10000 1 <= nums[i] < 2^31
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        我们想一下如果一个数字出现三次,那么他的二进制位表示的每一位(0或1)也出现了三次.
        如果把所有出现三次的数字的二进制表示的每一位都分别加起来,那么每一位的和都能被3整除

        我们把所有数字的二进制位的每一位加起来.若果某一位的和能被3整除,那么那个只出现一次的数字二进制表示中对应的那一位为0,否则为1
        '''
        bitSum = [0] * 32

        # 统计各位之和
        for i in nums:
            mask = 1
            for j in reversed(range(32)):
                if mask & i :
                    bitSum[j] += 1
                mask <<= 1
        res = 0
        for i in range(32):
            res <<= 1
            res += bitSum[i] % 3
        return res

if __name__ == "__main__":
    nums = [9, 3, 7, 9, 7, 9, 7]
    print(Solution().singleNumber(nums))
