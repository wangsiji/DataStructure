# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 7:47 下午
# @Author  : siJi
# @File    : 042_接雨水.py
# @Desc    :

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        单调栈
        '''
        if not height: return 0
        res = 0
        # 使用栈来存储条形块的索引下标。
        stack = []
        i = 0
        while i < len(height):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                # 找出界定高度
                h = min(height[stack[-1]], height[i]) - height[top]
                # 计算当前元素和栈顶元素的距离，准备进行填充操作
                w = i - stack[-1] - 1
                print(h * w)
                res += h * w
            stack.append(i)
            i += 1
        return res





if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
