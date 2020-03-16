# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 4:37 下午
# @Author  : siJi
# @File    : 面试题46_把数字翻译成字符串.py
# @Desc    : 动态规划、回溯


"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:
输入: 12258 输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
"""


class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        方法一 动态规划的 
        思路和 70. 爬楼梯 是一样的。
            爬楼梯这道题：爬楼梯时每次可以爬一层或两层，求有多少种不同的方法到达楼顶。
            而这道题换成了，每次可以选择一个数字或两个数字，用来合并成一个字符，求可以合成多少种字符串。
        状态方程：
            dp[i] = dp[i-1]  str(num)[i]和str(num)[i−1]不能合成一个字符 num[i−1]=='0' or str(num)[i-1:i+1] > '25'
            dp[i] = dp[i-1] + dp[i-2] num[i]和num[i−1]能合成一个字符
            1<=i<=len(str(num)) 
        base case:
            dp[1] = 1
        '''
        # s = str(num)
        # dp = [1 for _ in range(len(s)+1)]
        # for i in range(1, len(s)):
        #     if s[i-1] == "0" or s[i-1:i+1] > "25":
        #         dp[i+1] = dp[i]
        #     else:
        #         dp[i+1] = dp[i] + dp[i-1]
        # return dp[-1]

        '''
        方法二 回溯  
        绝大部分树形问题（多叉树或者是二叉树）都可以通过回溯解决，而这道题抽象为树模型后就是：求一颗二叉树从根结点到达叶子结点的路径总数。
            因为每次可能的选择都只有两个，犹如二叉树的两个分支。栗如：
            对于数字 13 ，你第一次可以只选择一位，那就是 1 ，翻译成字符就是 b；你也可以两位都选，那就是 13 , 翻译成字符为 n。
            所以最多就只有两个选择：走左子树或走右子树，走到叶子结点就返回 1 ，代表这条路径可以到达终点。
        '''

        def backtrance(s, pos):
            n = len(s)
            if pos == n:
                return 1
            if pos == n - 1 or s[pos] == '0' or s[pos:pos + 2] > '25':
                return backtrance(s, pos + 1)
            return backtrance(s, pos + 1) + backtrance(s, pos + 2)

        s = str(num)
        return backtrance(s, 0)


if __name__ == "__main__":
    num = 12258
    print(Solution().translateNum(num))
