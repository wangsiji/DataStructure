# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 6:05 下午
# @Author  : siJi
# @File    : 075_颜色分类.py
# @Desc    :


"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0] 输出: [0,0,1,1,2,2]

进阶：
一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p0 = 0  # 0的右边界
        p2 = len(nums) - 1  # 2的左边界
        curr = 0  # curr是当前考虑元素的下标
        while curr <= p2:
            # 交换第 curr个 和 第p0个 元素，并将指针都向右移。
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            # 交换第 curr个和第 p2个元素，并将 p2指针左移 。
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            # 将指针curr右移
            else:
                curr += 1
        print(nums)


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(Solution().sortColors(nums))
