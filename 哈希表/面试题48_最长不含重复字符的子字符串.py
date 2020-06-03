# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 11:35 下午
# @Author  : siJi
# @File    : 面试题48_最长不含重复字符的子字符串.py
# @Desc    :


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

"""

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        方法一：动态规划 + 哈希表
        状态定义：设动态规划列表dp ，dp[j] 代表以字符s[j] 为结尾的 “最长不重复子字符串” 的长度
        状态方程：固定右边界j ，设字符 s[j] 左边距离最近的相同字符为 s[i] ，即 s[i]=s[j] 
                dp[j] = dp[j-1] + 1, dp[j-1] < j-i 说明字符s[i] 在子字符串 dp[j−1] 区间之外
                dp[j] = j - i, dp[j-1] >= j-i 说明字符s[i] 在子字符串 dp[j−1] 区间之中
        """
        # lookup = {} # 统计各字符最后一次出现的索引位置
        # res = tmp = 0
        # for j in range(len(s)):
        #     i = lookup.get(s[j], -1)  # 获取索引i
        #     lookup[s[j]] = j
        #     tmp = tmp + 1 if tmp < j - i else j - i
        #     res = max(res, tmp)
        # return res
        """
        方法二：双指针 + 哈希表 本质上与方法一类似，不同点在于左边界i 的定义。
        哈希表 dic 统计： 指针j遍历字符s ，哈希表统计字符 s[j] 最后一次出现的索引 。
        更新左指针i ： 根据上轮左指针 i 和 dic[s[j]] ，每轮更新左边界 i ，保证区间 [i+1,j] 内无重复字符且最大。
        """
        lookup = {}
        res = 0
        i = -1
        for j in range(len(s)):
            if s[j] in lookup:
                i = max(lookup[s[j]], i)
            lookup[s[j]] = j
            res = max(res, j - i)
        return res


if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
