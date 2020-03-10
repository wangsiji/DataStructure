# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 7:22 下午
# @Author  : siJi
# @File    : 面试题20_表示数值的字符串.py
# @Desc    :

"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"及"-1E-16"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""


# TODO
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        p = re.compile(r'^[\+\-]?\d+[\.eE]?-?\d+$')
        return bool(p.match(s.strip()))


if __name__ == "__main__":
    s = "0"
    print(Solution().isNumber(s))
