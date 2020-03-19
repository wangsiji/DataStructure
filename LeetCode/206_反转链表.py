# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 11:14 下午
# @Author  : siJi
# @File    : 206_反转链表.py
# @Desc    :
"""
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶: 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
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

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
        print("")


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        方法一 双指针
        '''
        latter, former = None, head
        while former:
            cur = former.next
            former.next = latter
            latter, former = former, cur
        return latter


def travel(head):
    """遍历链表"""
    cur = head
    res = []
    if not head:
        return res
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


if __name__ == "__main__":
    ll = LinkList()
    nums = [1, 2, 3, 4, 5]
    for num in nums:
        ll.append(num)
    print(travel(ll.head))
    # print(Solution().reverseList(ll.head))
    print(travel(Solution().reverseList(ll.head)))
