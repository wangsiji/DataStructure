# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 7:35 下午
# @Author  : siJi
# @File    : 面试题52_两个链表的第一个公共节点.py
# @Desc    :


"""
输入两个链表，找出它们的第一个公共节点。
    如果两个链表没有交点，返回 null.
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

例1：
    输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    输出：Reference of the node with value = 2
"""


# Definition for singly-linked list.
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


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1

def travel( head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


if __name__ == "__main__":
    headA, headB = LinkList(), LinkList()
    listA = [0, 9, 1, 3, 4]
    listB = [3, 2, 4]
    for num in listA:
        headA.append(num)
    for num in listB:
        headB.append(num)
    ll = Solution().getIntersectionNode(headA.head, headB.head)
    print(travel(ll))
