# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 9:33 上午
# @Author  : siJi
# @File    : 049_字母异位词分组.py
# @Desc    :

"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        '''
        方法一：排序数组分类
        当且仅当它们的排序字符串相等时，两个字符串是字母异位词
        '''
        # import collections
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return ans.values()
        '''
        方法二：按计数分类
        '''
        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
