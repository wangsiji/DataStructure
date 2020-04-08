# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 8:40 下午
# @Author  : siJi
# @File    : 022_括号生成.py
# @Desc    : 递归

"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
# TODO

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''
        方法一 暴力
        '''
        def generateParenthesis(n):
            combinations = list()
            generateAll([0 for _ in range(2 * n)], 0, combinations)
        def generateAll(current, pos, res):
            if pos == len(current):
                if valid(current):res.append(current)

        def valid():
            pass
        if n == 0: return [""]
        res = []
        for c in range(n):
            pass
        # '''
        # 方法二 回溯法
        # '''
        # def backtrack(res, cur, left,right, max):
        #
if __name__ == "__main__":
    print(Solution().generateParenthesis(3))