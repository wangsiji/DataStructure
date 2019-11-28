# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 10:21 下午
# @Author  : siJi
# @File    : 005_最长回文子串.py
# @Desc    :

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad" 输出: "bab" 注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd" 输出: "bb"
"""


class Solution(object):
    def isPalindromic(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """暴力法，超出时间限制，时间复杂度:O(n**3), 空间复杂度:O(1)"""
        max_len = 0
        ans = ""
        if len(s) < 2:
            return s
        for i in range(len(s) - 1):
            for j in range(i+1, len(s)+1):
                print(i, j, s[i:j])
                if self.isPalindromic(s[i:j]) and max_len < j-i:
                    max_len = j-i
                    ans = s[i:j]
        return ans


if __name__ == "__main__":
    s = "bb"
    print(Solution().longestPalindrome(s))
