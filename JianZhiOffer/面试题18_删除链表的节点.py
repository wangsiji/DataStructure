# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 10:45 上午
# @Author  : siJi
# @File    : 面试题18_删除链表的节点.py
# @Desc    : 链表

"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。 返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:
输入: head = [4,5,1,9], val = 5 输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2:
输入: head = [4,5,1,9], val = 1 输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node  # 私有属性

    def add(self, item):
        # 先创建一个保存item值的节点
        node = ListNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self.__head
        # 将链表的头_head指向新节点
        self.__head = node

    def get_link(self):
        return self.__head


class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)  # 设置伪结点
        dummy.next = head
        if head.val == val:
            return head.next
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            head = head.next
        return dummy.next

    def travel(self, head):
        cur = head
        while cur is not None:
            print(cur.val)
            cur = cur.next


if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    head = ll.get_link()
    print(Solution().deleteNode(head, 3))
