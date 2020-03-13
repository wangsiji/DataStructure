# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 10:30 下午
# @Author  : siJi
# @File    : 面试题65_不用加减乘除做加法.py
# @Desc    :

"""
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:
输入: a = 1, b = 1 输出: 2
 
提示： a, b 均可能是负数或 0 结果不会溢出 32 位整数
"""

"""
Python-位操作( &、 | 、^、~ 、>>、 <<)
    &：按位与操作，只有 1 &1 为1，其他情况为0。可用于进位运算。
    |：按位或操作，只有 0|0为0，其他情况为1。
    ~：逐位取反。
    ^：异或，相同为0，相异为1。可用于加操作（不包括进位项）。
    <<：左移操作，2的幂相关
    >>：右移操作，2的幂相关
"""

"""
https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/
1. a + b 的问题拆分为 (a 和 b 的无进位结果) + (a 和 b 的进位结果)
2. 无进位加法使用异或运算计算得出
3. 进位结果使用与运算和移位运算计算得出
4. 循环此过程，直到进位为0
"""

"""
位运算中的加法:(相同位为 0，不同位为 1 的异或运算)
    0 + 0 = 0 0 + 1 = 1 1 + 0 = 1 1 + 1 = 0（进位 1）
异或的一个重要特性是无进位加法:
    a = 5 = 0101
    b = 4 = 0100
    a + b = 1001
    a ^ b = 0001
使用与操作获得进位:
    a & b = 0100
"""


# TODO
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 计算进位
        while b != 0:
            a = a ^ b
            b = (a & b) << 1
            print(a, b)


if __name__ == "__main__":
    a = 4
    b = 5
    print(Solution().add(a, b))
