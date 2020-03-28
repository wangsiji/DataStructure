# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 12:04 上午
# @Author  : siJi
# @File    : 排序_归并排序.py
# @Desc    :

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


if __name__ == "__main__":
    nums = [1, 5, 8, 6, 3, 4]

    print(merge_sort(nums))
