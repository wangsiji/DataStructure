# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 4:52 下午
# @Author  : siJi
# @File    : 347_前K个高频元素.py
# @Desc    : 堆


"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

说明：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''
        堆中添加一个元素的复杂度是 O(log(k))，要进行 N 次复杂度是 O(N)。
        最后一步是输出结果，复杂度为 O(klog(k))。

        时间复杂度：O(Nlog(k))。Counter 方法的复杂度是O(N)，建堆和输出的复杂度是 O(Nlog(k))。
                因此总复杂度为 O(N+Nlog(k))=O(Nlog(k))。
        空间复杂度：O(N)，存储哈希表的开销。
        '''
        import heapq
        import collections
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))