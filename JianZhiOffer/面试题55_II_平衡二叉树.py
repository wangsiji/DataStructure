# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 11:18 上午
# @Author  : siJi
# @File    : 面试题55_II_平衡二叉树.py
# @Desc    :

"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""


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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        自底向上的递归
        '''
        def helper(root):
            # An empty tree is balanced and has height -1
            if not root:
                return True, -1
            # Check subtrees to see if they are balanced.
            leftIsBalanced, leftHeight = helper(root.left)
            if not leftIsBalanced:
                return False, 0
            rightIsBalanced, rightHeight = helper(root.right)
            if not rightIsBalanced:
                return False, 0
            # If the subtrees are balanced, check if the current tree is balanced
            return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        return helper(root)[0]


if __name__ == "__main__":
    tree = Tree()
    nums = [1, 2, 2, 3, 3, None, None, 4, 4]
    for num in nums:
        tree.add(num)
    print(Solution().isBalanced(tree.root))
