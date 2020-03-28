# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 10:35 下午
# @Author  : siJi
# @File    : 面试题19_正则表达式匹配.py
# @Desc    :


"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:
输入: s = "aa" p = "a" 输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入: s = "aa" p = "a*" 输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入: s = "ab" p = ".*" 输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入: s = "aab" p = "c*a*b" 输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入: s = "mississippi" p = "mis*is*p*." 输出: false


s 可能为空，且只包含从 a-z 的小写字母。 p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
"""


def isMatch(text, pattern):
    # 第一步，我们暂时不管正则符号，如果是两个普通的字符串进行比较，如何进行匹配
    # 递归思想
    if not pattern:
        return not text
    fist_match = bool(text) and pattern[0] == text[0]
    return fist_match and isMatch(text[1:], pattern[1:])


def isMatchByDot(text, pattern):
    # 二、处理点号「.」通配符
    # 点号可以匹配任意一个字符
    if not pattern:
        return not text
    fist_match = bool(text) and pattern[0] in {text[0], "."}
    return fist_match and isMatch(text[1:], pattern[1:])


def isMatchByStar(text, pattern):
    # 三、处理「*」通配符
    # 星号通配符可以让前一个字符重复任意次数，包括零次。那到底是重复几次呢？
    if not pattern:
        return not text
    fist_match = bool(text) and pattern[0] in {text[0], "."}
    # 写递归的技巧是管好当下，之后的事抛给递归。
    if len(pattern) >= 2 and pattern[1] == "*":
        # 发现 '*' 通配符
        # 星号前面的那个字符到底要重复几次呢？这需要计算机暴力穷举来算，假设重复 N 次吧。
        # 不管N是多少，当前的选择只有两个：匹配0次、匹配1次。
        return isMatch(text, pattern[2:]) or fist_match and isMatch(text[1:], pattern)
    else:
        # 未发现 '*' 通配符
        return fist_match and isMatch(text[1:], pattern[1:])


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        '''
        方法一 回溯算法
        首先，我们考虑只有 '.' 的情况。这种情况会很简单：我们只需要从左到右依次判断 s[i] 和 p[i] 是否匹配。
        如果有星号，它会出现在 p[1] 的位置，这时有两种情况：
            星号代表匹配 0 个前面的元素。如 '##' 和 a*##，这时我们直接忽略 p 的 a*，比较 ## 和 ##；
            星号代表匹配一个或多个前面的元素。如 aaab 和 a*b，这时我们将忽略 s 的第一个元素，比较 aab 和 a*b。
        以上任一情况忽略掉元素进行比较时，剩下的如果匹配，我们认为 s 和 p 是匹配的。
        '''
        # # 边界条件
        # if not p:
        #     return not s
        # # 第一个字母是否匹配
        # first_match = bool(s and p[0] in {s[0], '.'})
        # # 如果 p 第二个字母是 *
        # if len(p) >= 2 and p[1] == "*":
        #     return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        # else:
        #     return first_match and self.isMatch(s[1:], p[1:])

        '''
        方法二 动态规划
        状态: dp[i][j] 表示的状态是 s 的前 i 项和 p 的前 j 项是否匹配。
        状态方程:
            dp[i][j] = dp[i-1][j-1]             # s[i]=p[j] or p[j]="."
            dp[i][j] = dp[i][j-2]               # p[j]="*" ,p[j-1] != s[i] 星号前一个字符匹配不上，星号匹配了 0 次
            dp[i][j] = dp[i-1][j] or dp[i][j-2] # p[j]="*" ,p[j-1] == s[i] or p[j-1] == '.'
            dp[i][j] = False                    # else
        '''
        if not p: return not s
        # s = "" p=".*"
        if not s and len(p) == 1: return False

        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        # 初始状态
        dp[0][0] = True
        dp[0][1] = False
        for c in range(2, n):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]
        for r in range(1, m):
            i = r - 1
            for c in range(1, n):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':  # ‘*’前面的字符匹配s[i] 或者为'.'
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:  # ‘*’匹配了0次前面的字符
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False
        return dp[m - 1][n - 1]



if __name__ == "__main__":
    s = "aab"
    p = "c*a*b"
    print(Solution().isMatch(s, p))