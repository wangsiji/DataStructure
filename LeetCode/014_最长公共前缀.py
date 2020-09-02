# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 8:23 上午
# @Author  : siJi
# @File    : 014_最长公共前缀.py
# @Desc    :


"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。

示例1:
输入: ["flower","flow","flight"] 输出: "fl"

示例2:
输入: ["dog","racecar","car"] 输出: "" 解释: 输入不存在公共前缀。

说明: 所有输入只包含小写字母a-z
"""


class Solution(object):
    def _lcp(self, str1, str2):
        """两个字符串的最长公共前缀"""
        length, index = min(str1, str2), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

    def longestCommonPrefix1(self, strs):
        """方法一 python特性"""
        res = ""
        if len(strs) == 0:
            return res
        for tup in list(zip(*strs)):
            if len(set(tup)) == 1:
                res += tup[0]
            else:
                return res
        return res

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        """方法二 横向扫描"""
        if not strs:
            return ""
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self._lcp(prefix, strs[i])
            if not prefix:
                break
        return prefix

    def longestCommonPrefix3(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """方法三 纵向扫描"""
        if not strs:
            return ""
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        return strs[0]




        """方法四 分治"""


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix3(strs))
