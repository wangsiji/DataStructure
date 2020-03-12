# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 9:14 上午
# @Author  : siJi
# @File    : 面试题64_求1+2+…+n.py
# @Desc    :

"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：
输入: n = 3 输出: 6

示例 2：
输入: n = 9 输出: 45
 
限制： 1 <= n <= 10000
"""

"""
使用递归解法最重要的是指定返回条件，但是本题无法直接使用 if 语句来指定返回条件
条件与 && 具有短路原则，即在第一个条件语句为 false 的情况下不会去执行第二个条件语句。
A && B
A 为 true，则返回表达式 B 的 bool 值
A 为 false，则返回 false

"""


class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        方法一 if else
        '''
        # if n == 1:
        #     return n
        # else:
        #     return n + self.sumNums(n-1)
        '''
        递归
        '''
        # n = 0 false 执行左边
        # n > 0 true 执行右边
        return n and n + self.sumNums(n - 1)


if __name__ == "__main__":
    print(Solution().sumNums(3))
