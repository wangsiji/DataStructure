# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 11:04 下午
# @Author  : siJi
# @File    : 面试题25_合并两个排序的链表.py
# @Desc    : 链表、递归

"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
输入：1->2->4, 1->3->4 输出：1->1->2->3->4->4

限制： 0 <= 链表长度 <= 1000
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


def travel(head):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        方法一 递归
        终止条件：两条链表分别名为 l1 和 l2，当 l1 为空或 l2 为空时结束
        返回值：每一层调用都返回排序好的链表头
        本级递归内容：如果 l1 的 val 值更小，则将 l1.next 与排序好的链表头相接，l2 同理
        """
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
        """
        方法二 迭代
        """
        prehead = ListNode(-1)  # 哨兵节点
        prev = prehead # 维护一个 prev 指针，我们需要做的是调整它的 next 指针
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if not l2 else l2
        return prehead.next


if __name__ == "__main__":
    l1 = LinkList()
    l1.append(1)
    l1.append(2)
    l1.append(4)
    l2 = LinkList()
    l2.append(1)
    l2.append(3)
    l2.append(4)
    merge_ll = Solution().mergeTwoLists(l1.head, l2.head)

