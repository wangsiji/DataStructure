# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 10:51 上午
# @Author  : siJi
# @File    : 树_二叉树的遍历.py
# @Desc    :

"""
https://blog.csdn.net/Monster_ii/article/details/82115772?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
树的遍历是树的一种重要的运算。
所谓遍历是指对树中所有结点的信息的访问，即依次对树中每个结点访问一次且仅访问一次，我们把这种对所有节点的访问称为遍历（traversal）。
那么树的两种重要的遍历模式是深度优先遍历和广度优先遍历,深度优先一般用递归，广度优先一般用队列。
一般情况下能用递归实现的算法大部分也能用堆栈来实现。
"""

"""
深度优先遍历
    深度优先搜索(Depth First Search)是沿着树的深度遍历树的节点，尽可能深的搜索树的分支。

深度遍历有重要的三种方法。
    这三种方式常被用于访问树的节点，它们之间的不同在于访问每个节点的次序不同。
    这三种遍历分别叫做先序遍历（preorder），中序遍历（inorder）和后序遍历（postorder）
    
先序遍历 
    在先序遍历中，我们先访问根节点，然后递归使用先序遍历访问左子树，再递归使用先序遍历访问右子树
    根节点->左子树->右子树
    
中序遍历 
    在中序遍历中，我们递归使用中序遍历访问左子树，然后访问根节点，最后再递归使用中序遍历访问右子树
    左子树->根节点->右子树

后序遍历 
    在后序遍历中，我们先递归使用后序遍历访问左子树和右子树，最后访问根节点
    左子树->右子树->根节点
 
      1         先序遍历 1,2,4,5,3,6,7
  2       3     中序遍历 4,2,5,1,6,3,7
4   5   6   7   后序遍历 4,5,2,6,7,3,1
"""

"""
广度优先遍历(层次遍历)
    从树的root开始，从上到下从从左到右遍历整个树的节点
"""



class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self):
        self.root = None

    def tree(self):
        return self.root

    def add(self, x):
        node = Node(x)
        # 根节点为空
        if not self.root:
            self.root = node
            return
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                if not cur.lchild:
                    cur.lchild = node
                    return
                elif not cur.rchild:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def breadth_travel(self):
        """广度优先遍历(层次遍历)"""
        if not self.root:
            return
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                print(cur.elem)
                if cur.lchild:
                    queue.append(cur.lchild)
                if cur.rchild:
                    queue.append(cur.rchild)
        pass


def preorder(root):
    if not root:
        return
    print(root.elem)
    preorder(root.lchild)
    preorder(root.rchild)


def inorder(root):
    if not root:
        return
    inorder(root.lchild)
    print(root.elem)
    inorder(root.rchild)


def postorder(root):
    if not root:
        return
    postorder(root.lchild)
    postorder(root.rchild)
    print(root.elem)


if __name__ == "__main__":
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(6)
    tree.add(2)
    tree.add(4)
    tree = tree.tree()

    print(inorder(tree))
