# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 11:38 上午
# @Author  : siJi
# @File    : 019_删除链表的倒数第N个节点.py
# @Desc    :


"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：你能尝试使用一趟扫描实现吗？
"""
#TODO

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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 设置哑结点
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    head = LinkList()
    for num in nums:
        head.append(num)
    print(Solution().removeNthFromEnd(head.head, 2))