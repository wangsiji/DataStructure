# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 7:47 上午
# @Author  : siJi
# @File    : 002_两数相加.py
# @Desc    : 链表


"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None

    def append(self, x):
        node = ListNode(x)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node


def travel(head):
    res = []
    if not head:
        return None
    else:
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
    return res


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        cur = pre
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            cur.next = ListNode(1)
        return pre.next


if __name__ == "__main__":
    num1 = [2, 4]
    # num1 = [None]
    num2 = [5, 6, 3, 2]
    l1 = LinkList()
    l2 = LinkList()
    for num in num1:
        l1.append(num)
    for num in num2:
        l2.append(num)
    print(Solution().addTwoNumbers(l1.head, l2.head))
    print(travel(Solution().addTwoNumbers(l1.head, l2.head)))
