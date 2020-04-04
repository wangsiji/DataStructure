# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 6:24 下午
# @Author  : siJi
# @File    : 148_排序链表.py
# @Desc    :

"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
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
        return res
    else:
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        归并排序
        '''
        if not head or not head.next: return head
        # cut the LinkedList at the mid index.
        # 快慢双指针法，奇数个节点找到中点，偶数个节点找到中心左边的节点。
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # save and cut.
        mid, slow.next = slow.next, None
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        # 双指针法合并，建立辅助ListNode h 作为头部。
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next


if __name__ == "__main__":
    nums = [4, 2, 1, 3]
    head = LinkList()
    for num in nums:
        head.append(num)
    print(Solution().sortList(head.head))
