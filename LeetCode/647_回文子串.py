# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 3:41 下午
# @Author  : siJi
# @File    : 647_回文子串.py
# @Desc    :

"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:
输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".

示例 2:
输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

注意:输入的字符串长度不会超过1000。
"""

# TODO
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        方法一 从中心往两侧延伸
        '''
        # n = len(s)
        # ans = 0
        # # 在长度为 N 的字符串中，可能的回文串中心位置有 2N-1 个：字母，或两个字母中间。
        # for center in range(2 * n - 1):
        #     left = int(center / 2)
        #     right = int(left + center % 2)
        #     print(center, left, right)
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         ans += 1
        #         left -= 1
        #         right += 1
        # return ans


        '''
        方法二 动态规划 
        dp[i][j] 代表str[i] - str[j]是否是回文子串
        状态转移方程：
            dp[i][j] = dp[i+1][j-1] && str[i]==str[j]
        '''
        res = 0




if __name__ == "__main__":
    s = "aaa"
    print(Solution().countSubstrings(s))
