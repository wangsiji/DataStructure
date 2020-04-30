# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 12:04 上午
# @Author  : siJi
# @File    : 快速排序.py
# @Desc    :

"""
从数列中挑出一个元素，称为"基准"（pivot），
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
"""


def quick_sort(nums):
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if i < pivot]
        greater = [i for i in nums[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


numsA = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(quick_sort(numsA))