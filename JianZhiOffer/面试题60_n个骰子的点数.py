# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 4:43 下午
# @Author  : siJi
# @File    : 面试题60_n个骰子的点数.py
# @Desc    : 动态规划、迭代、递归

"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:
输入: 1 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

示例 2:
输入: 2 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

限制：1 <= n <= 11
"""


class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """

        '''
        方法一 动态规划
        表示状态:
            dp[i][j]表示投掷完 i 枚骰子后，点数 j 的出现次数
            1<=i<=n  n<=j<=6n
        状态方程:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j-2] + dp[i-1][j-3] + dp[i-1][j-4] + dp[i-1][j-5] + dp[i-1][j-6]
        base case:
            dp[1][j] = 1
        '''
        # dp = [[0 for _ in range(6 * n)] for _ in range(n)]
        # for i in range(6):
        #     dp[0][i] = 1
        # for i in range(1, n):
        #     for j in range(i, 6 * (i + 1)):
        #         for k in range(1, 7):
        #             if j - k >= i - 1:
        #                 dp[i][j] += dp[i - 1][j - k]
        # res = dp[-1][n - 1:]
        # count = sum(res)
        # return [float(i / count) for i in res]
        '''
        方法二 迭代
        '''
        # tmp = [0] + [1] * 6 + [0] * (6 * n - 6)
        # for _ in range(n - 1):
        #     for i in range(6 * n, 0, -1):
        #         tmp[i] = sum(tmp[max(i - 6, 0): i])
        # return list(filter(lambda a: a != 0, list(map(lambda a: a / 6 ** n, tmp))))

        '''
        方法三 递归
        '''

        def diceCnt(n):
            if n == 1:
                return [0] + [1] * 6
            cnts = diceCnt(n - 1) + [0] * 6
            for i in range(6 * n, 0, -1):
                cnts[i] = sum(cnts[max(i - 6, 0): i])
            return cnts

        return list(filter(lambda a: a != 0, list(map(lambda a: a / 6 ** n, diceCnt(n)))))


if __name__ == "__main__":
    print(Solution().twoSum(2))
