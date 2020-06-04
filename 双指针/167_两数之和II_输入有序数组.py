# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 9:46 上午
# @Author  : siJi
# @File    : 167_两数之和II_输入有序数组.py
# @Desc    :

"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:
返回的下标值（index1 和 index2）不是从零开始的。 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例:
输入: numbers = [2, 7, 11, 15], target = 9 输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        使用两个指针，初始分别位于第一个元素和最后一个元素位置，比较这两个元素之和与目标值的大小。
            如果和等于目标值，我们发现了这个唯一解。
            如果比目标值小，我们将较小元素指针增加一。
            如果比目标值大，我们将较大指针减小一。
        """
        i = 1
        j = len(numbers)
        while i < j:
            if numbers[i-1] + numbers[j-1] == target:
                return [i, j]
            elif numbers[i-1] + numbers[j-1] > target:
                j -= 1
            else:
                i += 1

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
