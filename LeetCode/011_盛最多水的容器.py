# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 9:12 下午
# @Author  : siJi
# @File    : 011_盛最多水的容器.py
# @Desc    : 中等 双指针

"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """暴力法，超出时间限制，时间复杂度:O(n**2), 空间复杂度:O(1)"""
        # maxarea = 0
        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         maxarea = max(maxarea, min(height[j], height[i]) * (j - i))
        # return maxarea

        """双指针法，时间复杂度:O(n), 空间复杂度:O(1)"""
        left = 0
        right = len(height) - 1
        maxarea = 0
        while left < right:
            if height[left] < height[right]:
                maxarea = max(maxarea, height[left] * (right - left))
                left += 1
            else:
                maxarea = max(maxarea, height[right] * (right - left))
                right -= 1
        return maxarea


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
