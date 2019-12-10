# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 7:12 上午
# @Author  : siJi
# @File    : 392_判断子序列.py
# @Desc    : 动态规划

"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc" 返回 true.

示例 2:
s = "axc", t = "ahbgdc" 返回 false.

后续挑战 :
如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
"""

"""
DP定义：dp[i][j]表示长度为i的字符串s是否为长度为j的字符串t的子序列。
状态转移方程：
if(s.charAt(i)==t.charAt(j)){
　　dp[i][j] = dp[i-1][j-1];
}else{
　　dp[i][j] = dp[i][j-1];
}
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """双指针"""
        # i = j = 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # return i == len(s)
        """动态规划"""
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            for j in range(len(t) + 1):
                # s为空或者t为空
                if not i or not j:
                    dp[i][j] = True if i == 0 else False
                else:
                    if s[i-1] == t[i-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = dp[i][j-1]
        return dp


if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))
