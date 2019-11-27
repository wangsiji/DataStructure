# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 12:03 上午
# @Author  : siJi
# @File    : 排序_选择排序.py
# @Desc    : 排序

"""
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
"""


def selection_sort(alist):
    # 需要进行len(alist) - 1次选择操作
    for i in range(len(alist) - 1):
        # 记录最小位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i + 1, len(alist)):
            # 使min_index为最小值，遇到比min_index小的值就赋值于min_index
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]  # 交换最小值到左边

    return alist


if __name__ == "__main__":
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    print(selection_sort(alist))
