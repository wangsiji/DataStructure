# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 7:33 下午
# @Author  : siJi
# @File    : 253_会议室2.py
# @Desc    :

"""
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],…] (si < ei)，
为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:
输入: [[0, 30],[5, 10],[15, 20]]
输出: 2

示例 2:
输入: [[7,10],[2,4]]
输出: 1
"""


class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()
        res = []
        for i in intervals:
            if not res or res[-1][1] > i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return len(res)

if __name__ == "__main__":
    intervals = [[7,10],[2,4]]
    print(Solution().minMeetingRooms(intervals))
