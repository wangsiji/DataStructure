# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 11:32 上午
# @Author  : siJi
# @File    : 016_最接近的三数之和.py
# @Desc    : 排序和双指针


"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)  # 排序
        res = nums[0] + nums[1] + nums[2]  # 初始化
        for i in range(len(nums)):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                ans = nums[i] + nums[L] + nums[R]
                if abs(ans - target) <= abs(res - target):
                    res = ans
                if ans == target:
                    return res
                elif ans < target:
                    L += 1
                else:
                    R -= 1
        return res


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution().threeSumClosest(nums, target))
