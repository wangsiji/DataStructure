# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 5:38 下午
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
    if not head:
        return
    else:
        res = []
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
        print(travel(head))



if __name__ == "__main__":
    nums = [-1, 5, 3, 4, 0]
    head = LinkList()
    for num in nums:
        head.append(num)
    print(Solution().sortList(head.head))

