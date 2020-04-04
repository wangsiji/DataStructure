# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 7:02 下午
# @Author  : siJi
# @File    : 056_合并区间.py
# @Desc    :

"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals.sort()
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(i[1],res[-1][1])
        return res

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(Solution().merge(intervals))