# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 11:27 上午
# @Author  : siJi
# @File    : 461_汉明距离.py
# @Desc    : 位运算

"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意： 0 ≤ x, y < 231.

示例:
输入: x = 1, y = 4
输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        '''
        方法一：内置位计数功能
        x    0001
        y    0100
        x^y  0101
        ^ 相同为0 相异为1
        '''
        # return bin(x ^ y).count('1')

        '''
        方法二：移位
        ^ 相同为0 相异为1
        为了计算等于 1 的位数，可以将每个位移动到最左侧或最右侧，然后检查该位是否为 1。
        '''
        xor = x ^ y
        distance = 0
        while xor:
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance



if __name__ == "__main__":
    x = 1
    y = 4
    print(Solution().hammingDistance(x, y))
