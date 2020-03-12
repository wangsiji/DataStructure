# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 12:15 上午
# @Author  : siJi
# @File    : 面试题29_顺时针打印矩阵.py
# @Desc    : 数组

"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]] 输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：
0 <= matrix.length <= 100 0 <= matrix[i].length <= 100
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        [1,2,3,6,9,8,7,4,5]
        """
        '''
        左 右 上 下  l r t d 
        '''
        if not matrix:
            return []
        l, r, t, d, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            # 从左向右
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > d:
                break
            # 从上向下
            for i in range(t, d + 1):
                res.append(matrix[i][r])
            r -= 1
            if r < l:
                break
            # 从右向左
            for i in range(r, l - 1, -1):
                res.append(matrix[d][i])
            d -= 1
            if d < t:
                break
            # 从左向上
            for i in range(d, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))
