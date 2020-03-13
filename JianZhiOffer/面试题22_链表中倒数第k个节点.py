# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 6:28 下午
# @Author  : siJi
# @File    : 面试题22_链表中倒数第k个节点.py
# @Desc    : 双指针、链表

"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

示例：
给定一个链表: 1->2->3->4->5, 和 k = 2. 返回链表 4->5.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None

    def add(self, x):
        node = ListNode(x)
        node.next = self.head
        self.head = node

    def append(self, item):
        """尾部添加元素"""
        node = ListNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if not self.head:
            self.head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
        print("")

    def length(self):
        """统计长度"""
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def get_head(self):
        return self.head


class Solution(object):
    def travel(self, head):
        """遍历链表"""
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next
        print("")

    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        latter, former = head, head
        for _ in range(k):
            former = former.next
        while former:
            latter, former = latter.next, former.next
        return latter


if __name__ == "__main__":
    ll = LinkList()
    print("*" * 10)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    head = ll.get_head()
    print(Solution().getKthFromEnd(head, 2))
