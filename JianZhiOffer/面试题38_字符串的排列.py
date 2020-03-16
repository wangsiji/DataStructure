# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 11:20 上午
# @Author  : siJi
# @File    : 面试题38_字符串的排列.py
# @Desc    :

"""
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc" 输出：["abc","acb","bac","bca","cab","cba"]

限制： 1 <= s 的长度 <= 8
"""
# TODO

class Solution(object):
    def stringSort(self, s, tmp, res):
        if len(s) == 1:
            tmp.append(s[0])
            res.append("".join(tmp))
            tmp.pop()
            return
        for i in range(len(s)):
            if i and s[i] == s[0]:
                continue
            s[0], s[i] = s[i], s[0]
            tmp.append(s[0])
            self.stringSort(s[1:], tmp, res)
            tmp.pop()
            s[i], s[0] = s[0], s[i]

    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        '''
        回溯法解决
            第一步,求所有可能出现在第一个位置的字符,即把第一个字符和后面所有的字符进行交换
            第二步,固定住第一个字符,求后面字符的全排列.这时候我们仍把后面的字符分成两部分: 
                后面字符的第一个字符以及这个字符后面的所有字符.
                然后把第一个字符逐一和它后面的字符交换.
            第三步,算法最后的结果可能会有重复的情况出现,我们使用python自带的set()函数来去重
        '''
        res = []
        if not s:
            return []
        s = list(s)
        tmp = []
        self.stringSort(s, tmp, res)
        return list(set(res))


if __name__ == "__main__":
    s = "abc"
    print(Solution().permutation(s))
