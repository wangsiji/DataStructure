# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 4:41 下午
# @Author  : siJi
# @File    : 279_完全平方数.py
# @Desc    : 动态规划、BFS

"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:
输入: n = 12 输出: 3  解释: 12 = 4 + 4 + 4.

示例 2:
输入: n = 13 输出: 2 解释: 13 = 4 + 9.
"""

"""
初始化
    dp = [0,1,2,...,n], 长度为n+1, 最多次数就是全由1构成
状态方程：
    dp[i] = min(dp[i], dp[i-j*j]+1) i表示当前数字，j*j表示平方数
"""


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        方法一 动态规划
        '''
        # dp = [i for i in range(n + 1)]
        # for i in range(2, n + 1):
        #     for j in range(1, int(i ** 0.5) + 1):
        #         dp[i] = min(dp[i], dp[i - j * j] + 1)
        # return dp[-1]

        '''
        方法二 广度优先搜索
            当每一次都可以判断出多种情况，有多次的时候就适合用BFS-广度优先遍历
        使用BFS应注意：
            队列：用来存储每一轮遍历得到的节点；
            标记：对于遍历过的节点，应该将它标记，防止重复遍历。

            我们将它第一个平方数可能出现的情况做分析 只要 i * i < n 就行
            再在此基础上进行二次可能出现的平方数分析
            
        注意：为了节省遍历的时间，曾经（ n - 以前出现的平方数） 这个值出现过，则在此出现这样的数时直接忽略。
        '''
        from collections import deque
        if n == 0:
            return 0
        # 初始化队列、访问元组、路径长度
        queue = deque([n])
        visited = set()
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                tmp = queue.pop()
                for i  in range(1, int(tmp ** 0.5) + 1):
                    x = tmp - i ** 2
                    if x == 0:
                        return step
                    if x not in visited:
                        queue.appendleft(x)
                        visited.add(x)
        return step


if __name__ == "__main__":
    n = 12
    print(Solution().numSquares(n))
