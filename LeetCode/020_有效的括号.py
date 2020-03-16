# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 8:44 下午
# @Author  : siJi
# @File    : 020_有效的括号.py
# @Desc    : 栈

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。左括号必须以正确的顺序闭合。 注意空字符串可被认为是有效字符串。

示例 1:
输入: "()" 输出: true

示例 2:
输入: "()[]{}" 输出: true

示例 3:
输入: "(]" 输出: false

示例 4:
输入: "([)]" 输出: false

示例 5:
输入: "{[]}" 输出: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        lookup = ["()", "{}", "[]"]
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and (stack[-2] + stack[-1]) in lookup:
                stack.pop()
                stack.pop()
        return len(stack) == 0


if __name__ == "__main__":
    s = "{[]}"
    print(Solution().isValid(s))
