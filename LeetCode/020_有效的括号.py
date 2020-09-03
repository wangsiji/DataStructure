# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 2:46 下午
# @Author  : siJi
# @File    : 020_有效的括号.py
# @Desc    :


"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。左括号必须以正确的顺序闭合。 注意空字符串可被认为是有效字符串。

示例 1:
输入: "()" 输出: true

示例2:
输入: "()[]{}" 输出: true

示例3:
输入: "(]" 输出: false

示例4:
输入: "([)]" 输出: false

示例5:
输入: "{[]}" 输出: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = ["[]", "{}", "()"]
        stack = []
        for i in range(len(s)):
            if stack and (stack[-1] + s[i]) in lookup:
                stack.pop()
            else:
                stack.append(s[i])
        return not stack


if __name__ == "__main__":
    s = "(]"
    print(Solution().isValid(s))
