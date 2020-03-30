# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 9:43 下午
# @Author  : siJi
# @File    : 面试题05_替换空格.py
# @Desc    : 字符串

"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：输入：s = "We are happy." 输出："We%20are%20happy."

限制：0 <= s 的长度 <= 10000
"""

"""
先遍历找到多少个空格，然后开辟数组填充
"""


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        时间复杂度：O(n)。遍历字符串 s 一遍。
        空间复杂度：O(n)。额外创建字符数组
        '''
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
