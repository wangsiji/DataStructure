# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 1:13 下午
# @Author  : siJi
# @File    : 063_不同路径II.py
# @Desc    : 动态规划

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。说明：m 和 n 的值均不超过 100。

示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""

"""
状态方程：
    dp[i][j] = dp[i][j - 1] + dp[i - 1][j] if obstacleGrid[i][j] != 1 else 0
base case:
    dp[0][j] =  int(dp[0][j - 1] == 1 and obstacleGrid[0][j] == 0)
    dp[i][0] =  int(dp[i - 1][0] == 1 and obstacleGrid[i][0] == 0)
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        """
        时间复杂度 ： O(M×N)。长方形网格的大小是 M×N，而访问每个格点恰好一次。
        空间复杂度 ： O(1)。我们利用 obstacleGrid 作为 DP 双指针，因此不需要额外的空间。
        """
        # # 如果第一个格点是 1，说明有障碍物，那么机器人不能做任何移动，返回结果 0
        # if obstacleGrid[0][0] == 1:
        #     return 0
        # obstacleGrid[0][0] = 1
        # # 第一行
        # for i in range(1, len(obstacleGrid[0])):
        #     obstacleGrid[0][i] = int(obstacleGrid[0][i] == 0 and obstacleGrid[0][i - 1] == 1)
        # # 第一列
        # for i in range(1, len(obstacleGrid)):
        #     obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)
        # for i in range(1, len(obstacleGrid)):
        #     for j in range(1, len(obstacleGrid[0])):
        #         # 如果这个点有障碍物，设值为 0 ，这可以保证不会对后面的路径产生贡献
        #         if obstacleGrid[i][j] == 0:
        #             obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        #         else:
        #             obstacleGrid[i][j] = 0
        # return obstacleGrid[-1][-1]

        '''DP'''
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        dp[0][0] = 1
        for i in range(1, len(obstacleGrid)):
            dp[i][0] = int(dp[i - 1][0] == 1 and obstacleGrid[i][0] == 0)
        for j in range(1, len(obstacleGrid[0])):
            dp[0][j] = int(dp[0][j - 1] == 1 and obstacleGrid[0][j] == 0)
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j] if obstacleGrid[i][j] != 1 else 0

        return dp[-1][-1]


if __name__ == "__main__":
    obstacleGrid = [[0, 0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
