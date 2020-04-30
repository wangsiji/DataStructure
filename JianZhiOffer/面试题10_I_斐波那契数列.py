# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 10:55 下午
# @Author  : siJi
# @File    : 面试题10_I_斐波那契数列.py
# @Desc    : 动态规划

"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
F(0) = 0,   F(1) = 1 F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2 输出：1

示例 2：
输入：n = 5 输出：5
 
提示：0 <= n <= 100
"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''方法一 迭代'''
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # a, b = 0, 1
        # for _ in range(2, n+1):
        #     a, b = b, a + b
        # return b

        '''方法二 递归'''
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # return self.fib(n - 1) + self.fib(n - 2)


if __name__ == "__main__":
    # 0 1 1 2 3 5 8
    print(Solution().fib(6))
