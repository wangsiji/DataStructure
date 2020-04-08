# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 8:56 下午
# @Author  : siJi
# @File    : 101_对称二叉树.py
# @Desc    :


"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        方法一 递归
        递归结束条件：
            都为空指针则返回 true
            只有一个为空则返回 false
        递归过程：
            判断两个指针当前节点值是否相等
            判断 A 的右子树与 B 的左子树是否对称
            判断 A 的左子树与 B 的右子树是否对称
        短路：
            在递归判断过程中存在短路现象，也就是做 与 操作时，如果前面的值返回 false 则后面的不再进行计算
        '''
        # def isMirror(t1, t2):
        #     if not t1 and not t2:
        #         return True
        #     if not t1 or not t2:
        #         return False
        #     return (t1.val == t2.val) & isMirror(t1.left, t2.right) & isMirror(t1.right, t2.left)
        # return  isMirror(root, root)

        '''
        方法二 迭代
        '''
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
    nums = [1, 2, 2, 3, 4, 4, 3]
    tree = Tree()
    for num in nums:
        tree.add(num)
    print(Solution().isSymmetric(tree.root))
