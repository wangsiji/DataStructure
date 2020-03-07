# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 9:31 下午
# @Author  : siJi
# @File    : 面试题04_二维数组中的查找.py
# @Desc    : 双指针


"""
一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
import numpy as np


# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         # write code here
#         """贪心算法"""
#         # for i in range(len(array)):
#         #     for j in range(len(array[0])):
#         #         if array[i][j] == target:
#         #             return True
#         # return False
#         """
#         分治解题思路
#         从右上角(或者左下角)开始查找：
#             - 如果target更大，指针下移
#             - 如果target更小，指针左移
#         """
#         # # 右上角
#         # i = 0
#         # j = len(array[0]) - 1
#         # while i < len(array[0]) and j >= 0:
#         #     if target > array[i][j]:
#         #         i += 1
#         #     elif target < array[i][j]:
#         #         j -= 1
#         #     else:
#         #         return True
#         # return False


class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False


if __name__ == "__main__":
    # target = 12
    # array = np.arange(12).reshape([3, 4])
    target = 7
    matrix = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    print(Solution().findNumberIn2DArray( matrix,target))
