# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 4:34 下午
# @Author  : siJi
# @File    : 617_合并二叉树.py
# @Desc    : 树、递归、迭代

"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。
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
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        '''
        方法一 递归
            对这两棵树同时进行前序遍历，并将对应的节点进行合并。
        '''
        # if not t1:
        #     return t2
        # if not t2:
        #     return t1
        # t1.val += t2.val
        # t1.left = self.mergeTrees(t1.left, t2.left)
        # t1.right = self.mergeTrees(t1.right, t2.right)
        # return t1

        '''
        方法二 迭代
        '''
        # 如果 t1和t2中，只要有一个是null，函数就直接返回
        if not t1:
            return t2
        if not t2:
            return t1
        queue = [t1, t2]
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            node1.val = node1.val + node2.val
            # 如果r1和r2的左子树都不为空，就放到队列中
            # 如果r1的左子树为空，就把r2的左子树挂到r1的左子树上
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            elif not node1.left:
                node1.left = node2.left
            # 对于右子树也是一样的
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)
            elif not node1.right:
                node1.right = node2.right
        return t1



if __name__ == "__main__":
    num1 = [1, 3, 5]
    num2 = [1, 2, 4, 7]
    tree1 = Tree()
    tree2 = Tree()
    for num in num1:
        tree1.add(num)
    for num in num2:
        tree2.add(num)
    merge_tree = Solution().mergeTrees(tree1.root, tree2.root)
    print(breadth_travel(merge_tree))
