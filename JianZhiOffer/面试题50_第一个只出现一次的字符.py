# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 11:06 上午
# @Author  : siJi
# @File    : 面试题50_第一个只出现一次的字符.py
# @Desc    :


"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

示例:
s = "abaccdeff" 返回 "b"
s = "" 返回 " "
 
限制：0 <= s 的长度 <= 50000
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''普通字典'''
        # lookup = {}
        # for i in s:
        #     lookup[i] = lookup.get(i, 0) + 1
        # for i in s:
        #     if lookup[i] == 1:
        #         return i
        # return " "
        import collections
        lookup = collections.OrderedDict()
        for i in s:
            lookup[i] = lookup.get(i, 0) + 1
        for key, value in lookup.items():
            if value == 1:
                return key

        return " "


if __name__ == "__main__":
    s = "abaccdeff"
    print(Solution().firstUniqChar(s))
