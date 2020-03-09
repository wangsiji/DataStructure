# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 10:47 下午
# @Author  : siJi
# @File    : 面试题48_最长不含重复字符的子字符串.py
# @Desc    : 滑动窗口


"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
输入: "abcabcbb" 输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb" 输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew" 输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：s.length <= 40000
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        方法一 动态规划
        dp[i] 以第i个字符为结尾的不包含重复字符的子字符串的最长长度.
        s[i]之前没有出现过: dp[i] = dp[i-1] + 1 
        s[i]之前有出现过: 假设两者距离为d 
            (1) d<=dp[i-1], 则dp[i] = d
            (2) d>dp[i-1] , 则dp[i] = dp[i-1] + 1 
        """
        # if not s:
        #     return 0
        # lookup = {}
        # dp = [0 for _ in range(len(s) + 1)]
        # for i in range(len(s)):
        #     if s[i] not in lookup:
        #         dp[i + 1] = dp[i] + 1
        #     else:
        #         distance = i - lookup[s[i]]
        #         if distance <= dp[i]:
        #             dp[i + 1] = distance
        #         else:
        #             dp[i + 1] = dp[i] + 1
        #     lookup[s[i]] = i
        # return max(dp)

        """
        方法二 滑动窗口+双指针
        1. 如果当前字符不在滑动窗口内的时候,比较之前的存储的最大结果与当前的滑动窗口的大小,取最大的
        2. 如果当前字符在滑动串口内时,将low指针向前移直到当前字符不在滑动窗口内
        """
        # res = 0
        # low = 0
        # for high in range(len(s)):
        #     if s[high] not in s[low:high]:
        #         res = max(res, high - low + 1)
        #     else:
        #         while s[high] in s[low:high]:
        #             low += 1
        # return res

        """
        方法二 滑动窗口+哈希表
        时间复杂度为O(n),空间复杂度为O(n)
        """
        left = 0  # 左边窗口
        max_len = 0  # 最大长度
        lookup = dict()
        for right in range(len(s)):
            # 是判断s[j]相同元素上次出现的位置
            if s[right] in lookup:
                # 如果 left 大，说明[left,right-1]中没有与s[right]相同的元素，起始位置仍取left；
                # 如果 left 小，则在[left,right-1]中有了与s[right]相同的元素，所以起始位置变为lookup[s[right]]+1，即[lookup[s[right]]+1,right]
                left = max(left, lookup[s[right]])
            max_len = max(max_len, right - left + 1)
            lookup[s[right]] = right + 1
        return max_len


if __name__ == "__main__":
    s = "tmmzuxt"
    print(Solution().lengthOfLongestSubstring(s))
