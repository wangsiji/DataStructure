# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 2:42 下午
# @Author  : siJi
# @File    : 160_相交链表.py
# @Desc    :

"""
编写一个程序，找到两个单链表相交的起始节点。

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
         从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
         在 A 中，相交节点前有 2 个节点；
         在 B 中，相交节点前有 3 个节点。

注意：
    如果两个链表没有交点，返回 null.
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""


# TODO


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
        return res
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


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


if __name__ == "__main__":
    listA = [4, 1, 8, 4, 5]
    listB = [5, 0, 1, 8, 4, 5]
    lA, lB = LinkList(), LinkList()
    for num in listA:
        lA.append(num)
    for num in listB:
        lB.append(num)

    a = lA.head
    b = lA.head

    print(a == b)
    # print(travel(lA.head))
    # print(travel(lB.head))
    # print(travel(Solution().getIntersectionNode(lA.head, lB.head)))
