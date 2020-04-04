# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 3:10 下午
# @Author  : siJi
# @File    : 221_最大正方形.py
# @Desc    :


"""

在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""

"""
状态方程：
    dp[i][j]表示的是由 1 组成的最大正方形的边长；
    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
base case:
    dp[i][0] = 1 if matrix[i][0]=="1" else 0
    dp[0][j] = 1 if matrix[0][j]=="1" else 0
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not i or not j:
                    dp[i][j] = 1 if matrix[i][j] == "1" else 0
                else:
                    if matrix[i][j] == "1":
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                res = max(res, dp[i][j])
        return res * res


if __name__ == "__main__":
    matrix = [["1"]]
    print(Solution().maximalSquare(matrix))
