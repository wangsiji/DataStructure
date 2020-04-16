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

'''https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pass
        '''
        方法一 暴力解法
        我们可以生成所有 2**2n个 '(' 和 ')' 字符构成的序列，然后我们检查每一个是否有效即可。
        
        时间复杂度：O（n * 2 ** 2n）
        空间复杂度：O(n)
        '''
        # def generate(A):
        #     """
        #     为了生成所有序列，我们可以使用递归。长度为 n 的序列就是在长度为 n-1 的序列前加一个 '(' 或 ')'。
        #     """
        #     if len(A) == 2 * n:
        #         if valid(A):
        #             res.append("".join(A))
        #     else:
        #         A.append("(")
        #         generate(A)
        #         A.pop()
        #         A.append(")")
        #         generate(A)
        #         A.pop()
        # def valid(A):
        #     bal = 0
        #     for c in A:
        #         if c == "(":
        #             bal += 1
        #         else:
        #             bal -= 1
        #         if bal < 0: return False
        #     return bal == 0
        #
        # res = []
        # generate([])
        # return res

        '''
        方法二 回溯法
        我们可以只在序列仍然保持有效时才添加 '(' or ')'，而不是像 方法一 那样每次添加。
        
        可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点
        
        如果左括号数量不大于n，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号
        '''


        '''
        ['((()))', '(()())', '(())()', '()(())', '()()()']
        '''
        res = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                res.append("".join(S))
                return
            if left < n :
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return res


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
