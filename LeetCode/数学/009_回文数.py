# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 12:29 下午
# @Author  : siJi
# @File    : 009_回文数.py
# @Desc    : 数学

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""

"""
思考：
    1. 将数字转换为字符串，并检查字符串是否为回文。需要额外的非常量空间。
    2. 将数字本身反转，然后将反转后的数字与原始数字进行比较，如果它们是相同的，那么这个数字就是回文。
        整数溢出问题: 为了避免数字反转可能导致的溢出问题，为什么不考虑只反转数字的一半？
        如何知道反转数字的位数已经达到原始数字位数的一半？
        
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 负数和最后一位为0的非0数字
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        res = 0
        while x > res:
            res = res * 10 + x % 10
            x = x // 10
        # 当数字长度为奇数时，我们可以通过 revertedNumber/10 去除处于中位的数字。
        return x == res or x == res // 10


if __name__ == "__main__":
    x = 121
    print(Solution().isPalindrome(x))
