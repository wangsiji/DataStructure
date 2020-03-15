# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 4:19 下午
# @Author  : siJi
# @File    : 面试题66_构建乘积数组.py
# @Desc    : 对称遍历

"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

示例:
输入: [1,2,3,4,5] 输出: [120,60,40,30,24]

提示：
所有元素乘积之和不会溢出 32 位整数 a.length <= 100000
"""


class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        left, right = [1] * len(a), [1] * len(a)
        # left [1, 1, 2, 6, 24]
        for i in range(1, len(a)):
            left[i] = left[i - 1] * a[i - 1]
        # right [120, 60, 20, 5, 1]
        for j in reversed(range(len(a) - 1)):
            right[j] = right[j+1] * a[j+1]
        for i in range(len(a)):
            left[i] = left[i] * right[i]
        return left


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    print(Solution().constructArr(a))
