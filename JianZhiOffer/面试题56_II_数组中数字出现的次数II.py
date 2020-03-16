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
        pass


if __name__ == "__main__":
    nums = [9, 1, 7, 9, 7, 9, 7]
    print(Solution().singleNumber(nums))
