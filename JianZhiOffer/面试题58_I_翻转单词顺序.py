# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 4:01 下午
# @Author  : siJi
# @File    : 面试题58_I_翻转单词顺序.py
# @Desc    : 双指针、字符串

"""
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
例如输入字符串"I am a student. "，则输出"student. a am I"。

示例 1：
输入: "the sky is blue" 输出: "blue is sky the"

示例 2：
输入: "  hello world!  " 输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入: "a good   example" 输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 
说明：
无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""
from functools import reduce


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''方法一 使用split和reverse'''
        # return " ".join(s.split()[::-1])
        '''方法二
            1.翻转数组
            2.翻转单个单词
            3.清除多余空格
        '''
        print(list(s))
        reverse_s_arr = self._reverse(list(s), 0, len(s) - 1)
        reverse_word = self._word_reverse(reverse_s_arr)
        print(reverse_word)
        return " ".join(reverse_word)

    def _reverse(self, arr, i, j):
        """
        翻转数组
        :return:
        """
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr

    def _word_reverse(self, arr):
        """
        翻转单个单词
        :return:
        """
        new_arr = []
        # 快慢指针
        i = 0
        j = 0
        while i < len(arr):
            # 单词首字母
            while i < len(arr) and arr[i] == " ":
                i += 1
            j = i
            # 单词末位置
            while j < len(arr) and arr[j] != " ":
                j += 1
            self._reverse(arr, i, j - 1)
            if arr[i:j]:
                new_arr.append(''.join(arr[i:j]))
            i = j
        return new_arr


if __name__ == "__main__":
    s = "  hello world!  "
    print(Solution().reverseWords(s))

