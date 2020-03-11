# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 11:05 下午
# @Author  : siJi
# @File    : 347_前K个高频元素.py
# @Desc    : 中等｜


"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2 输出: [1,2]

示例 2:
输入: nums = [1], k = 1 输出: [1]

说明：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
"""

"""
堆排序处理海量数据的topK，分位数非常合适，因为它不用将所有的元素都进行排序，只需要比较和根节点的大小关系就可以了，同时也不需要一次性将所有的数据都加载到内存。

原则：最大堆求前n小，最小堆求前n大。
前k小：构建一个k个数的最大堆，当读取的数小于根节点时，替换根节点，重新塑造最大堆
前k大：构建一个k个数的最小堆，当读取的数大于根节点时，替换根节点，重新塑造最小堆

总体思路
建立字典遍历一次统计出现频率
取前k个数，构造规模为k的最小堆 minheap
遍历规模k之外的数据，大于堆顶则入堆，维护规模为k的最小堆 minheap
如需按频率输出，对规模为k的堆进行排序          
"""

import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 方法一
        # count = collections.Counter(nums)
        # return heapq.nlargest(k, count.keys(), key=count.get)
        # 方法二

        def heapify(arr, n, i):
            pass

        # 哈希表字典统计出现频率
        lookup = {}
        for item in nums:
            lookup[item] = lookup.get(item, 0) + 1


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
