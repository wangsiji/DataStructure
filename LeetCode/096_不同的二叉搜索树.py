# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 3:26 下午
# @Author  : siJi
# @File    : 096_不同的二叉搜索树.py
# @Desc    : 动态规划

"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:
输入: 3 输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

"""
1. 假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则
    G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)
    
2. 当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，则
    f(i)=G(i−1)∗G(n−i)

3. 综合两个公式可以得到 卡特兰数 公式
    G(n)=G(0)∗G(n−1)+G(1)∗(n−2)+...+G(n−1)∗G(0)
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0],dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i+1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


if __name__ == "__main__":
    print(Solution().numTrees(3))
