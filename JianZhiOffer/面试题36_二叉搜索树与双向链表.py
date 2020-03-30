# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 10:24 下午
# @Author  : siJi
# @File    : 面试题36_二叉搜索树与双向链表.py
# @Desc    :
# TODO

"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。
对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
"""


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, x):
        node = Node(x)
        if not self.root:
            self.root = node
            return
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


def travel(root):
    res = []
    if not root:
        return
    queue = [root]
    while queue:
        cur = queue.pop(0)
        res.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return res


class Solution(object):
    def treeToDoublyListCore(self, root):
        """
        root: 树的根结点
        return 双向链表的头节点和尾节点
        """
        # 根为空，那么 对应的双向链表的 头节点 和 尾节点 也为空
        if not root:
            return None, None
        # 左子树 对应的 双向链表的头节点和尾节点
        left_head, left_tail = self.treeToDoublyListCore(root.left)
        # 右子树 对应的 双向链表的头节点和尾节点
        right_head, right_tail = self.treeToDoublyListCore(root.right)
        # 根的 左节点 与 左子树的尾节点 互相连接
        # 根的 右节点 与 右子树的头节点 互相连接
        root.left, root.right = left_tail, right_head
        if left_tail:
            left_tail.right = root
        if right_head:
            right_head.left = root
        # 左子树的头节点 如果存在则作为当前 双向链表的头节点，否则使用 根节点。尾节点同理。
        return left_head if left_head else root, right_tail if right_tail else root

    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        """
         递归遍历
         时间复杂度：O(N)，所有节点遍历一次。
         空间复杂度：O(N)，当二叉搜索树退化为链表时，树的深度为 N.
         """
        head, tail = self.treeToDoublyListCore(root)
        # 改造成循环双向链表
        if head and tail:
            head.left, tail.right = tail, head
        return head

if __name__ == "__main__":
    nums = [4, 2, 5, 1, 3]
    tree = Tree()
    for num in nums:
        tree.add(num)
    print(Solution().treeToDoublyList(tree.root))
