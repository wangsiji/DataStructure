# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 10:16 下午
# @Author  : siJi
# @File    : 面试题26_树的子结构.py
# @Desc    :

"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2
给定的树 B：
   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1] 输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1] 输出：true

限制：0 <= 节点个数 <= 10000
"""

#TODO
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        pass