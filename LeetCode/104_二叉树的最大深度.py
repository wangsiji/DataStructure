# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 11:47 上午
# @Author  : siJi
# @File    : 104_二叉树的最大深度.py
# @Desc    :

"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
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


def breadth_travel(tree):
    res = []
    if not tree:
        return res
    else:
        queue = [tree]
        while queue:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
    return res


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        方法一 递归
        '''
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        '''
        方法二 迭代
        '''
        if not root:
            return 0
        queue = [(1, root)]
        depth =  0
        while queue:
            cur_depth, node = queue.pop(0)
            if node:
                depth = max(cur_depth, depth)
                queue.append((cur_depth + 1, node.left))
                queue.append((cur_depth+1,node.right))
        return depth

if __name__ == "__main__":
    tree = Tree()
    nums = [3, 9, 20, None, None, 15, 7]
    for num in nums:
        tree.add(num)
    print(breadth_travel(tree.root))
