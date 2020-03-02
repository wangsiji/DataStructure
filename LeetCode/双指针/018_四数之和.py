# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 5:21 下午
# @Author  : siJi
# @File    : 018_四数之和.py
# @Desc    :

"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        # 去除异常
        if not nums or len(nums) < 4:
            return res
        nums = sorted(nums)  # 排序
        # 第一个数遍历
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 第二个数遍历
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 双指针
                L, R = j + 1, len(nums) - 1
                while L < R:
                    if nums[i] + nums[j] + nums[L] + nums[R] == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        L += 1
                        R -= 1
                    elif nums[i] + nums[j] + nums[L] + nums[R] < target:
                        L += 1
                    else:
                        R -= 1
        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    target = -1
    print(Solution().fourSum(nums, target))
