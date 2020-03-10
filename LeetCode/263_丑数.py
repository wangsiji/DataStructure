# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 9:16 上午
# @Author  : siJi
# @File    : 263_丑数.py
# @Desc    : 数学


"""
编写一个程序判断给定的数是否为丑数。丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:
输入: 6 输出: true 解释: 6 = 2 × 3

示例 2:
输入: 8 输出: true 解释: 8 = 2 × 2 × 2

示例 3:
输入: 14 输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数 7。

说明：
1 是丑数。 输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        '''就是不断的去和2，4，5进行相除，如果最终是1，那么就是true，如果中间无法整除，就是false'''
        if num <= 0:
            return False
        while True:
            if not num % 2:
                num /= 2
            elif not num % 3:
                num /= 3
            elif not num % 5:
                num /= 5
            elif num == 1:
                return True
            else:
                return False


if __name__ == "__main__":
    print(Solution().isUgly(8))