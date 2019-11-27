# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 12:03 上午
# @Author  : siJi
# @File    : 排序_插入排序.py
# @Desc    : 排序
"""
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
"""


def insert_sort(alist):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]

    return alist


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(insert_sort(alist))
