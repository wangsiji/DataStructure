# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 9:16 下午
# @Author  : siJi
# @File    : 面试题68_I_二叉搜索树的最近公共祖先.py
# @Desc    : 树、递归、迭代

"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 解释: 节点 2 和节点 8 的最近公共祖先是 6。

示例 2:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

说明:
    所有节点的值都是唯一的。
    p、q 为不同节点且均存在于给定的二叉搜索树中。
"""

"""
二叉搜索树（BST）的性质:
    1.节点 N 左子树上的所有节点的值都小于等于节点 N 的值
    2.节点 N 右子树上的所有节点的值都大于等于节点 N 的值
    3.左子树和右子树也都是 BST
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
        方法一 递归
        
        时间复杂度：O(N) 空间复杂度：O(N)
        
        思路：
            节点p，q 的最近公共祖先（LCA）是距离这两个节点最近的公共祖先节点。
            笔记：p 和 q 其中的一个在 LCA 节点的左子树上，另一个在 LCA 节点的右子树上。
            
        算法：
            1. 从根节点开始遍历树
            2. 如果节点 p 和节点 q 都在右子树上，那么以右孩子为根节点继续 1 的操作
            3. 如果节点 p 和节点 q 都在左子树上，那么以左孩子为根节点继续 1 的操作
            4. 如果条件 2 和条件 3 都不成立，这就意味着我们已经找到节 p 和节点 q 的 LCA 了
        '''
        # if p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # elif p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return root

        '''
        方法二 迭代 
        '''
        node = root
        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                return node
        return None


if __name__ == "__main__":
    tree = Tree()
    nums = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    for num in nums:
        tree.add(num)
    root = tree.root
    p = root.left
    q = root.right
    print(Solution().lowestCommonAncestor(root, p, q))
