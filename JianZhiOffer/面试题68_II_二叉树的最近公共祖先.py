# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 10:04 下午
# @Author  : siJi
# @File    : 面试题68_II_二叉树的最近公共祖先.py
# @Desc    :


"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 
说明: 所有节点的值都是唯一的。 p、q 为不同节点且均存在于给定的二叉树中。
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


def breadth_travel(root):
    if not root:
        return
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        '''
        DFS(后续遍历)
        递归
        思路：
            如果p和q分别是root的左右节点，那么root就是我们要找的最近公共祖先
            如果p和q都是root的左节点，那么返回lowestCommonAncestor(root.left,p,q)
            如果p和q都是root的右节点，那么返回lowestCommonAncestor(root.right,p,q)
        边界条件：
            如果root是null，则说明我们已经找到最底了，返回null表示没找到
            如果root与p相等或者与q相等，则返回root
            如果左子树没找到，递归函数返回null，证明p和q同在root的右侧，那么最终的公共祖先就是右子树找到的结点
            如果右子树没找到，递归函数返回null，证明p和q同在root的左侧，那么最终的公共祖先就是左子树找到的结点
        '''
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


if __name__ == "__main__":
    nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    tree = Tree()
    for num in nums:
        tree.add(num)
    root = tree.root
    p = root.left
    q = root.right
    print(Solution().lowestCommonAncestor(root, p, q).val)
