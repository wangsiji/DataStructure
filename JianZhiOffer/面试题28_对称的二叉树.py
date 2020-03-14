# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 1:18 下午
# @Author  : siJi
# @File    : 面试题28_对称的二叉树.py
# @Desc    : 树、递归、迭代

"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

示例 1：输入：root = [1,2,2,3,4,4,3] 输出：true

示例 2：输入：root = [1,2,2,null,3,null,3] 输出：false
 
限制：0 <= 节点个数 <= 1000
"""


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
    def isMirror(self, tree1, tree2):
        # 结束条件
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        # 递归过程：
        #     判断两个指针当前节点值是否相等
        #     判断 A 的右子树与 B 的左子树是否对称
        #     判断 A 的左子树与 B 的右子树是否对称
        return (tree1.val == tree2.val) and self.isMirror(tree1.left, tree2.right) and self.isMirror(tree1.right,
                                                                                                     tree2.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        方法一 递归
        递归结束条件：
            都为空指针则返回True
            只有一个为空则返回False
        递归过程：
            判断两个指针当前节点值是否相等
            判断 A 的右子树与 B 的左子树是否对称
            判断 A 的左子树与 B 的右子树是否对称
        短路：
            在递归判断过程中存在短路现象，也就是做 与 操作时，如果前面的值返回 false 则后面的不再进行计算
        时间复杂度：O(n)
        """
        # return self.isMirror(root, root)
        """
        方法二 迭代
        """
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            tree1 = queue.pop(0)
            tree2 = queue.pop(0)
            if not tree1 and not tree2:
                continue
            if not tree1 or not tree2:
                return False
            if tree1.val != tree2.val:
                return False
            queue = queue + [tree1.left, tree2.right, tree1.right, tree2.left]
        return True


if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(4)
    tree.add(3)
    tree = tree.tree()
    print(Solution().isSymmetric(tree))
