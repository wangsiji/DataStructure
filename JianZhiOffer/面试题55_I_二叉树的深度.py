# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 10:49 上午
# @Author  : siJi
# @File    : 面试题55_I_二叉树的深度.py
# @Desc    : 树、递归

"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, x):
        node = TreeNode(x)
        if not self.root:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                if not cur.left:
                    cur.left = node
                    return
                elif not cur.right:
                    cur.right = node
                    return
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)

    def breadth_travel(self):
        if not self.root:
            return
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                print(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 终止条件：root为空
        # 返回值：
        # 本级递归内容：
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    tree = Tree()
    tree.add(3)
    tree.add(9)
    tree.add(20)
    tree.add(None)
    tree.add(None)
    tree.add(15)
    tree.add(7)
    print(Solution().maxDepth(tree.root))
