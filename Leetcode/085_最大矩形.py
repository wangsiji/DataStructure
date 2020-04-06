# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 10:27 上午
# @Author  : siJi
# @File    : 085_最大矩形.py
# @Desc    :


"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        '''
        方法一 动态规划 - 使用柱状图的优化暴力方法
        '''
        # dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        # max_area = 0
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         # 每个点对应的最大宽度
        #         width = dp[i][j] = dp[i][j - 1] + 1 if matrix[i][j] == "1" else 0
        #         # 预计算最大宽度的方法事实上将输入转化成了一系列的柱状图，每一栏是一个新的柱状图。
        #         # 我们在针对每个柱状图计算最大面积。
        #         for k in range(i, -1, -1):
        #             width = min(width, dp[k][j])
        #             max_area = max(max_area, width * (i - k + 1))
        # return max_area
        '''
        方法二 使用柱状图 - 栈
        '''
        def LetCode(heights):
            stack = [-1]

            max_area = 0
            for i in range(len(heights)):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
                stack.append(i)

            while stack[-1] != -1:
                max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
            return max_area
        if not matrix: return 0

        max_area = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            # update maxarea with the maximum area from this row's histogram
            max_area = max(max_area, LetCode(dp))
        return max_area



if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(Solution().maximalRectangle(matrix))
