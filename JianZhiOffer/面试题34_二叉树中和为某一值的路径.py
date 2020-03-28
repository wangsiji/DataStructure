# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 10:22 下午
# @Author  : siJi
# @File    : 面试题34_二叉树中和为某一值的路径.py
# @Desc    :

"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示： 节点总数 <= 10000
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
            return
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


def travel(root):
    res = []
    if not root:
        return res
    else:
        queue = [root]
        while queue:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
    return res


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        '''
        先序遍历： 按照“根、左、右”的顺序，遍历树的所有节点。
        路径记录： 在先序遍历中，当 ① 根节点到叶节点形成的路径 且 ② 路径各节点值的和等于目标值 sum 时，记录此路径。
        '''
        res, path = [], []

        def helper(root, tar):
            # 递归出口：解决子问题
            if not root:
                return
            path.append(root.val)
            tar -= root.val
            # 如果节点为叶子节点，并且 sum == 0
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            helper(root.left, tar)
            helper(root.right, tar)
            # 处理完一个节点后，恢复初始状态，为node.left,  node.right操作
            path.pop()

        helper(root, sum)
        return res


if __name__ == "__main__":
    nums = [5, 4, 8, 11, 13, 4, 7, 2, 5, 1]
    tree = Tree()
    for num in nums:
        tree.add(num)
    print(travel(tree.root))
    print(Solution().pathSum(tree.root, 22))
