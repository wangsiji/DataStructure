# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 5:38 下午
# @Author  : siJi
# @File    : 064_最小路径和.py
# @Desc    :

"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7 解释: 因为路径 1→3→1→1→1 的总和最小。
"""

"""
状态方程：
    dp[i][j] = min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j]) # 表示第i行，第j个网格，最小的路径数字总合
base case:
    dp[0][j] = dp[0][j-1] + grid[i][j]
    dp[i][0] = dp[i-1][0] + grid[i][j]
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
        return dp[len(grid) - 1][len(grid[0]) - 1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))
