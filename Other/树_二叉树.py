# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 11:47 下午
# @Author  : siJi
# @File    : 树_二叉树.py
# @Desc    :


class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""

    def __init__(self, root=None):
        self.root = root

    def tree(self):
        return self.root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值,返回
        if not self.root:
            self.root = node
            return
        else:
            queue = [self.root]
            # 对已有的节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if not cur.lchild :
                    cur.lchild = node
                    return
                elif not cur.rchild:
                    cur.rchild = node
                    return
                else:
                    # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def breadth_travel(self):
        """
        广度优先遍历(层次遍历)
        从树的root开始，从上到下从从左到右遍历整个树的节点
        利用队列实现树的层次遍历
        """
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)


if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    print(tree.tree())
    print(tree.breadth_travel())
