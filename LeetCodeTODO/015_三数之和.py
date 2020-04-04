# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 8:47 上午
# @Author  : siJi
# @File    : 015_三数之和.py
# @Desc    : 排序和双指针

"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

"""


算法流程：
1. 特判，对于数组长度 n，如果数组为 null 或者数组长度小于 3，返回 []。
2. 对数组进行排序。
3. 遍历排序后数组：
    (1). 若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
    (2). 对于重复元素：跳过，避免出现重复解。
    (3). 令左指针 L=i+1，右指针 R=n−1，当 L<R 时，执行循环：
        a. 当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
        b. 若和大于0，说明 nums[R]太大, R左移
        c. 若和小于0，说明 nums[L]太小，L右移
复杂度分析：
    时间复杂度：O(n2)，数组排序 O(Nlog⁡N)，遍历数组 O(n)，双指针遍历 O(n)，总体 O(Nlog⁡N)+O(n)∗O(n)，O(n2)
    空间复杂度：O(1)
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # 对于数组长度 n，如果数组为 null 或者数组长度小于 3，返回 []
        if not nums or len(nums) < 3:
            return res
        # 排序
        nums = sorted(nums)
        print(nums)
        # 遍历排序后数组
        # i L=i+1 R=len(nums)-1
        for i in range(len(nums)):
            # 若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果
            if nums[i] > 0:
                return res
            # 对于重复元素：跳过，避免出现重复解
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 左、右指针
            L, R = i + 1, len(nums) - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L = L + 1
                    R = R - 1
                elif nums[i] + nums[L] + nums[R] < 0:
                    L = L + 1
                else:
                    R = R - 1
        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
