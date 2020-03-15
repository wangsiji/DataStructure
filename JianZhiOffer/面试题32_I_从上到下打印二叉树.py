# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 11:08 下午
# @Author  : siJi
# @File    : 面试题32_I_从上到下打印二叉树.py
# @Desc    : 队列 BFS 树


"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。


例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回：[3,9,20,15,7]

提示：节点总数 <= 1000
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


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
        res, queue = [], [root]
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


if __name__ == "__main__":
    nums = [3, 9, 20, None, None, 15, 7]
    tree = Tree()
    for num in nums:
        tree.add(num)
    root = tree.root
    print(Solution().levelOrder(root))
