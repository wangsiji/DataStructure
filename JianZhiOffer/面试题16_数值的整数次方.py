# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 9:49 上午
# @Author  : siJi
# @File    : 面试题16_数值的整数次方.py
# @Desc    : 递归

"""
Pow(x, n)
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:
输入: 2.00000, 10 输出: 1024.00000

示例 2:
输入: 2.10000, 3 输出: 9.26100

示例 3:
输入: 2.00000, -2 输出: 0.25000
解释: 2**-2 = 1/2**2 = 1/4 = 0.25

说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""


class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        '''
        方法一 暴力解法
        '''
        # if n < 0:
        #     n = -n
        #     x = 1 / x
        # res = 1
        # for _ in range(n):
        #     res *= x
        # return res

        '''
        方法二 递归
        时间复杂度：O(logn) 空间复杂度：O(logn)
        假定我们已经得到了 x**n 的结果, 如何得到 x**2n? ==> (x**n)*2 ==> 一次计算
        '''

        def fastPow(x, n):
            if n == 0:
                return 1.0
            half = fastPow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            n = -n
            x = 1 / x
        return fastPow(x, n)


if __name__ == "__main__":
    x = 2.00000
    n = 10
    print(Solution().myPow(x, n))
