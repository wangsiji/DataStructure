# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 8:21 下午
# @Author  : siJi
# @File    : 面试题54_二叉搜索树的第k大节点.py
# @Desc    :


"""
给定一棵二叉搜索树，请找出其中第k大的节点。


示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

限制：1 ≤ k ≤ 二叉搜索树元素个数
"""

"""
若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 
"""
# TODO

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def tree(self):
        return self.root

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


def breadth_travel(tree):
    """广度优先搜索"""
    if not tree:
        return
    else:
        queue = [tree]
        while queue:
            cur = queue.pop(0)
            print(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)


class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []

        def inorder(self, root):
            if not root:
                return
            self.inorder(root.left)
            res.append(root.val)
            self.inorder(root.right)
        inorder(root)
        return res
        pass


if __name__ == "__main__":
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(6)
    tree.add(2)
    tree.add(4)
    tree.add(None)
    tree.add(None)
    tree.add(1)
    tree = tree.tree()
    print(Solution().kthLargest(tree, 1))
