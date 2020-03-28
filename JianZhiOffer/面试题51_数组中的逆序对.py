# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 10:30 下午
# @Author  : siJi
# @File    : 面试题51_数组中的逆序对.py
# @Desc    :

# TODO
"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4] 输出: 5
 

限制：0 <= 数组长度 <= 50000
"""


def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pass
