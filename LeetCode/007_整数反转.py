# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 10:48 下午
# @Author  : siJi
# @File    : 007_整数反转.py
# @Desc    :


"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例1:
输入: 123 输出: 321

示例 2:
输入: -123 输出: -321

示例 3:
输入: 120 输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为[−2**31, 2**31− 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x >= 0 else -1
        p = flag * x
        res = 0
        MAX_VALUE = 2 ** 31 - 1  # 2147483647
        MIN_VALUE = - 2 ** 31  # -2147483648
        while p:
            pop = p % 10
            # 溢出问题解决
            if flag == 1:  # 最大值溢出
                if (res == MAX_VALUE // 10 and pop > MAX_VALUE % 10) or (res > MAX_VALUE // 10):
                    return 0
            else:  # 最小值溢出
                if (res == - MIN_VALUE // 10 and pop > -MIN_VALUE % 10) or (res > -MIN_VALUE // 10):
                    return 0
            res = res * 10 + pop
            p = p // 10
        return res * flag


if __name__ == "__main__":
    x = -123
    print(Solution().reverse(x))
