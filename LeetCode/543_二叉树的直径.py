# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:24 上午
# @Author  : siJi
# @File    : 543_二叉树的直径.py
# @Desc    : 深度优先搜索 、递归、 树

"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。
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


def breadth_travel(root):
    if not root:
        return None
    else:
        queue = [root]
        while queue:
            cur = queue.pop(0)
            print(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)


class Solution(object):
    def __init__(self):
        self.ans = 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        方法：深度优先搜索
        '''

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.ans = max(self.ans, l + r + 1)
            return max(l, r) + 1

        dfs(root)
        return self.ans - 1

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    tree = Tree()
    for num in nums:
        tree.add(num)
    print(Solution().diameterOfBinaryTree(tree.root))
