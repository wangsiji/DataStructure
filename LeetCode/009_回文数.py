# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 8:29 上午
# @Author  : siJi
# @File    : 009_回文数.py
# @Desc    :


"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121 输出: true

示例2:
输入: -121 输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10 输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:你能不将整数转为字符串来解决这个问题吗？
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
        return res == x or x == res // 10


if __name__ == "__main__":
    x = 121
    print(Solution().isPalindrome(x))
