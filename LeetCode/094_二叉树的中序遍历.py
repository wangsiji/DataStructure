# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 5:55 下午
# @Author  : siJi
# @File    : 094_二叉树的中序遍历.py
# @Desc    : 递归、迭代

"""
给定一个二叉树，返回它的中序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

"""
递归：
    前序遍历:打印-左-右
    中序遍历:左-打印-右
    后序遍历:左-右-打印
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


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        方法一 递归
        '''
        # res = []
        #
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)
        #
        # dfs(root)
        # return res

        '''
        方法二 迭代
        '''
        res = []
        stack = []
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res


if __name__ == "__main__":
    tree = Tree()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for num in nums:
        tree.add(num)
    print(Solution().inorderTraversal(tree.root))
