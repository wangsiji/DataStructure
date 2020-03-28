# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 10:20 下午
# @Author  : siJi
# @File    : 面试题33_二叉搜索树的后序遍历序列.py
# @Desc    :


"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：
输入: [1,6,3,2,5] 输出: false

示例 2：
输入: [1,3,2,6,5] 输出: true
 
提示：数组长度 <= 1000
"""


class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        '''
        后序遍历性质： [ 左子树 | 右子树 | 根节点 ] ，即遍历顺序为 “左、右、根” 。
        二叉搜索树性质： 左子树任意节点的值 < 根节点的值；右子树任意节点的值 > 根节点的值。
        '''

        def helper(i, j):
            if i >= j:
                return True
            # 左子树
            l = i
            while postorder[l] < postorder[j]:
                l += 1
            # 右子树
            m = l
            while postorder[m] > postorder[j]:
                m += 1
            return m == j and helper(i, l - 1) and helper(l, m - 1)

        return helper(0, len(postorder) - 1)


if __name__ == "__main__":
    postorder = [1, 3, 2, 6, 5]
    print(Solution().verifyPostorder(postorder))
