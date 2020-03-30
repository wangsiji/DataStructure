# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 10:27 下午
# @Author  : siJi
# @File    : 面试题41_数据流中的中位数.py
# @Desc    :

"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

示例 1：
输入：["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"] [[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]

示例 2：
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"] [[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
 
限制：最多会对 addNum、findMedia进行 50000 次调用。
"""

'''
方法一 排序：将添加的数保存在数组中，返回中位数时，只需将数组排序，返回中间位置数即可。
方法二：二分查找插入 假如每次插入一个值前数组已经排好序了呢？这样我们只需考虑每次将值插在合适的位置即可，
        所以使用二分查找来找到这个合适的位置，会将时间复杂度降低到O(n)（查找: O(logn)，插入:O(n)）。
方法三：优先队列
'''

'''

注意：Python 中没有大顶堆，只能将值取负保存在小顶堆来模拟。为了方便理解，将堆用优先队列表示
'''
import heapq
# TODO

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = [] # 前半部分
        self.min_heap = [] # 后半部分

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 将中位数左边的数保存在大顶堆中，右边的数保存在小顶堆中。这样我们可以在O(1) 时间内得到中位数。
        # 先加到大顶堆，再把大堆顶元素加到小顶堆
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        # 先加到小顶堆，再把小堆顶元素加到大顶堆
        else:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]



if __name__ == "__main___":
    # ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
    # [[],[1],[2],[],[3],[]]
    # [null,null,null,1.50000,null,2.00000]
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.s, obj.l)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
