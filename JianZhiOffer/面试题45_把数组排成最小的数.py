# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 9:49 上午
# @Author  : siJi
# @File    : 面试题45_把数组排成最小的数.py
# @Desc    : 排序、字符串

"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
输入: [10,2] 输出: "102"

示例 2:
输入: [3,30,34,5,9] 输出: "3033459"

提示:
0 < nums.length <= 100

说明:
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
"""

"""
根据题目的要求,两个数字m和n能拼接成数字mn和nm,
    如果mn < nm那么现在他们的相对位置是正确的,
    如果mn > nm,那么就需要将n移到m的前面,根据这样的特性我们能将整个数组进行排列,得到最终的结果.
比较的时候先将数据转换成str格式的,利用str格式的字符串直接比较就可以
"""


class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return None
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return "".join(nums)


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    print(Solution().minNumber(nums))
