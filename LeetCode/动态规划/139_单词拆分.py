# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 1:54 下午
# @Author  : siJi
# @File    : 139_单词拆分.py
# @Desc    :

"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。 你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"] 输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"] 输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。 注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]   输出: false
"""

"""
dp[i]表示字符串s的前i个字符能否拆分成wordDict

以“leetcode”为例，字典为“leet”和“code”，显然dp[4]为true,我们要的是dp[8] （即dp[sLen]）
观察可知dp[8]可以由dp[4]和字典推导来，就是知道了dp[4]为true，从s+4开始，枚举看之后的单词是否能与
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(Solution().wordBreak(s, wordDict))
