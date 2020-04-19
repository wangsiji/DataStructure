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
        方法一 动态规划
        dp[i][j]表示s[i:j]是否是回文
        状态转移方程：当 s[i] == s[j] && (j - i < 2 || dp[i + 1][j - 1]) 时，dp[i][j]=true，否则为false
            1.当只有一个字符时，比如a自然是一个回文串。
            2.当有两个字符时，如果是相等的，比如aa，也是一个回文串。
            3.当有三个及以上字符时，比如ababa这个字符记作串1，把两边的a去掉，也就是bab记作串2，可以看出只要串2是一个回文串，
              那么左右各多了一个a的串1必定也是回文串。所以当s[i]==s[j]时，自然要看dp[i+1][j-1]是不是一个回文串。
        '''
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        res = 0
        for i in range(len(s)):
            for j in range(i + 1):
                if s[i] == s[j] and (i- j < 2 or dp[j+1][i-1] ):
                    dp[i][j] = True
                    res += 1
        print(dp)
        return res


        # '''
        # 方法一 从中心往两侧延伸
        # '''
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


if __name__ == "__main__":
    s = "aaaaa"
    print(Solution().countSubstrings(s))
