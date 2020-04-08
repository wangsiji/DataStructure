# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 9:50 上午
# @Author  : siJi
# @File    : 226_翻转二叉树.py
# @Desc    :

"""
翻转一棵二叉树。

示例：
输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
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


class invertTree(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        '''
        方法一 递归
        '''
        # if not root:
        #     return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        '''
        方法二 迭代
        '''
        if not root:
            return None
        else:
            queue = [root]
            while queue:
                cur = queue.pop(0)
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            return root

if __name__ == "__main__":
    nums = [4, 2, 7, 1, 3, 6, 9]
    tree = Tree()
    for num in nums:
        tree.add(num)
    print(breadth_travel(tree.root))
    print(breadth_travel(invertTree().invertTree(tree.root)))
