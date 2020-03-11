# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 2:48 下午
# @Author  : siJi
# @File    : 二分查找.py
# @Desc    : 二分查找


def binary_search(list, item):
    left, right = 0, len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            left = mid + 1
        else:
            right = mid - 1


if __name__ == "__main__":
    list = [1, 3, 5, 7, 9]
    item = 3
    print(binary_search(list, item))
