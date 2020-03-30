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


class Solution(object):
    def partition(self):
        pass

    def randomized_partition(self):
        pass

    def randomized_selected(self):
        pass

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
        方法二 最小堆
        最小堆建立(需要o(n)时间复杂度)
        取出前k个数(每次取需要用logn时间重建堆)。时间复杂度为o(n)+o(k*logn)
        '''
        # import heapq
        # heapq.heapify(arr)
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(arr))
        # return res

        '''
        方法三 计数排序
        对于数组 arr = [0,0,0,3,8,5,5]
            我们把arr里面元素的值当做nums的下标，比如arr里面的8，我们可以在nums里把nums[8]置为1，如果8在arr里出现两次呢？那就再+1
            所以，nums经过处理后，把arr里面的值处理为如下[3,0,0,1,0,2,0,0,1]
        '''
        # nums = [0] * 1000
        # for num in arr:
        #     nums[num] += 1
        # res = []
        # i = 0
        # while len(res) < k:
        #     if nums[i] >=1:
        #         for j in range(nums[i]):
        #             res.append(i)
        #     i += 1
        # return res[:k]
        '''
        方法四 快速排序
        用快排partition划分，一直划中第k个数 最差情况O(kn)

        快速排序会根据分界值的下标递归处理划分的两侧，而这里我们只处理划分的一边。
        '''

        def helper(arr, k):
            if k > len(arr) or k <= 0:
                return []
            pivot = arr[0]
            left = [num for num in arr[1:] if num <= pivot]
            right = [num for num in arr[1:] if num > pivot]
            if len(left) == k - 1:
                return left + [pivot]
            elif len(left) > k - 1:
                return helper(left, k)
            else:
                return left + [pivot] + helper(right, k - len(left) - 1)

        return helper(arr, k)


if __name__ == "__main__":
    arr = [0,0,1,2,4,2,2,3,1,4]
    k = 8
    print(Solution().getLeastNumbers(arr, k))
