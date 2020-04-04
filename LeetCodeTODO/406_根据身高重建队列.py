# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 11:02 上午
# @Author  : siJi
# @File    : 406_根据身高重建队列.py
# @Desc    : 排序

"""
假设有打乱顺序的一群人站成一个队列。
每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例
输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        贪心算法：
        1 排序：
            按高度降序排列
            在同一高度的人中， 按k值的生序排列
        2 逐个地把它们放在输出队列中，索引等于它们的 k 值。
        
        时间复杂度：O(n**2)
        空间复杂度：O(n)
        '''
        # 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数
        # h倒序 k正序
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
            print(res)


if __name__ == "__main__":
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(Solution().reconstructQueue(people))
