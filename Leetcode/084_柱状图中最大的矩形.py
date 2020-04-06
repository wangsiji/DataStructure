# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 10:54 上午
# @Author  : siJi
# @File    : 084_柱状图中最大的矩形.py
# @Desc    :

"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例:
输入: [2,1,5,6,2,3]
输出: 10
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        '''
        方法一 暴力
        
        时间复杂度：O(n**3)
        空间复杂度：O(1)
        '''
        # max_area = 0
        # for i in range(len(heights)):
        #     for j in range(i, len(heights)):
        #         width = j - i + 1
        #         height = float("inf")
        #         for h in range(i, j + 1):
        #             height = min(height, heights[h])
        #         max_area = max(max_area, width * height)
        # return max_area
        '''
        方法二 暴力优化
        '''
        # max_area = 0
        # for i in range(len(heights)):
        #     height = float("inf")
        #     for j in range(i, len(heights)):
        #         width = j - i + 1
        #         height = min(height, heights[j])
        #         max_area = max(max_area, width * height)
        # return max_area

        '''
        方法三 分治
            1.确定了最矮柱子以后，矩形的宽尽可能往两边延伸
            2.在最矮柱子左边的最大面积矩形（子问题）
            3.在最矮柱子右边的最大面积矩形（子问题）
            
        时间复杂度：O(nlogn)
        空间复杂度：O(n)
        '''
        # def helper(heights, start, end):
        #     if start > end:
        #         return  0
        #     min_index = start
        #     for i in range(start, end+1):
        #         if heights[min_index] > heights[i]:
        #             min_index = i
        #     return max(heights[min_index]*(end-start+1), max(helper(heights, start, min_index-1), helper(heights, min_index+1, end)))
        # return  helper(heights, 0, len(heights) - 1)

        '''
        方法4 双指针
        是以i 为中心，向左找第一个小于 heights[i] 的位置 left_i；
                    向右找第一个小于于 heights[i] 的位置 right_i
                    即最大面积为 heights[i] * (right_i - left_i -1)
        '''
        # max_area = 0
        # for i in range(len(heights)):
        #     left = i
        #     right = i
        #     while left >= 0 and heights[left] >= heights[i]:
        #         left -= 1
        #     while right < len(heights) and heights[right] >= heights[i]:
        #         right += 1
        #     max_area = max(max_area, heights[i] * (right - left -1))
        # return max_area

        '''
        方法5 栈 
        单调递增栈
        https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode/
        '''
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            # 不断将柱子的序号放进栈中，直到遇到相邻柱子呈下降关系
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()]* (len(heights) - stack[-1] - 1))
        return max_area


if __name__ == "__main__":
    heights = [6,7,5,2,5,5,9,3]
    print(Solution().largestRectangleArea(heights))
