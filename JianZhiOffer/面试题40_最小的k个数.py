# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 8:30 上午
# @Author  : siJi
# @File    : 面试题40_最小的k个数.py
# @Desc    : 排序、快速排序、堆

"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2 输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1 输出：[0]
 
限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
"""
#TODO

class Solution(object):
    def quickSort(self, arr, start, end):
        pivot = arr[start]
        while start < end:
            while start < end and arr[start] < pivot:
                start += 1

    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''
        方法一 排序
        时间复杂度O(nlogn)
        '''
        # sorted_arr = sorted(arr)
        # return sorted_arr[:k]
        '''
        方法二 快速排序
        用快排partition划分，一直划中第k个数 最差情况O(kn)
        '''
        if k > len(arr) or k <= 0:
            return []

        start = 0
        end = len(arr) - 1

        '''
        方法三 最小堆
        最小堆建立(需要o(n)时间复杂度)
        取出前k个数(每次取需要用logn时间重建堆)。时间复杂度为o(n)+o(k*logn)
        '''
        # import heapq
        # heapq.heapify(arr)
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(arr))
        # return res


if __name__ == "__main__":
    arr = [7, 3, 2, 10, 4, 5, 6, 8, 1]
    k = 2
    print(Solution().getLeastNumbers(arr, k))
