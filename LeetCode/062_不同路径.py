# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 11:48 上午
# @Author  : siJi
# @File    : 062_不同路径.py
# @Desc    : 动态规划

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
说明：m 和 n 的值均不超过 100。

示例 1:
输入: m = 3, n = 2 输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3 输出: 28
"""

"""dp[i][j] 是到达 i, j 最多路径"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """时间复杂度：O(mn), 空间复杂度：O(mn)"""
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         # 对于第一行 dp[0][j]，或者第一列 dp[i][0]，由于都是在边界，所以只能为 1
        #         if not i or not j:
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[-1][-1]
        """
        优化一：由于dp[i][j] = dp[i-1][j] + dp[i][j-1]，
        因此只需要保留当前行与上一行的数据 (在动态方程中，即pre[j] = dp[i-1][j])，两行，空间复杂度O(2n)
        """
        # pre = [1] * n
        # cur = [1] * n
        # for i in range(1, m):
        #     for j in range(1, n):
        #         cur[j] = pre[j] + cur[j - 1]
        #     pre = cur[:]
        # return pre[-1]

        """
        优化二：cur[j] += cur[j-1], 即cur[j] = cur[j] + cur[j-1] 
        等价于思路二-->> cur[j] = pre[j] + cur[j-1]，因此空间复杂度为O(n).
        """
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]


if __name__ == "__main__":
    m = 7
    n = 3
    print(Solution().uniquePaths(m, n))
