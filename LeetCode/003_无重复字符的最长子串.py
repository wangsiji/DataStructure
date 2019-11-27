# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 12:56 下午
# @Author  : siJi
# @File    : 003_无重复字符的最长子串.py
# @Desc    : Sliding Window

"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。请注意，你的答案必须是子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0  # 左边窗口
        max_len = 0  # 最大长度
        lookup = dict()
        for right in range(len(s)):
            # 是判断s[j]相同元素上次出现的位置
            if s[right] in lookup:
                # 如果 left 大，说明[left,right-1]中没有与s[right]相同的元素，起始位置仍取i；
                # 如果 left 小，则在[left,right-1]中有了与s[right]相同的元素，所以起始位置变为lookup[s[right]]+1，即[lookup[s[right]]+1,right]
                left = max(left, lookup[s[right]])
            max_len = max(max_len, right - left + 1)
            lookup[s[right]] = right + 1
        return max_len


if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
