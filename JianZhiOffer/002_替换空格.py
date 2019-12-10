# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 9:43 下午
# @Author  : siJi
# @File    : 002_替换空格.py
# @Desc    : 字符串

"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

"""
先遍历找到多少个空格，然后开辟数组填充
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # 新数组
        new_arr = []
        for i in s:
            if i == " ":
                new_arr.append("%20")
            else:
                new_arr.append(i)
        return "".join(new_arr)


if __name__ == "__main__":
    s = "We Are Happy"
    print(Solution().replaceSpace(s))
