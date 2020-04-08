# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 1:55 下午
# @Author  : siJi
# @File    : 215_数组中的第K个最大元素.py
# @Desc    :


"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def helper(nums, k):
            if k > len(nums): return None
            pivot = nums[0]
            left = [i for i in nums[1:] if i >= pivot]
            right = [i for i in nums[1:] if i < pivot]
            if len(left) == k - 1:
                return pivot
            elif len(left) < k-1:
                return helper(right, k-len(left)-1)
            else:
                return helper(left, k)

        return helper(nums, k)


if __name__ == "__main__":
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(Solution().findKthLargest(nums, k))
