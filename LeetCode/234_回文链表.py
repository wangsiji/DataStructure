# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 10:04 上午
# @Author  : siJi
# @File    : 234_回文链表.py
# @Desc    :

"""
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶： 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
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
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        方法一 双指针
        '''
        pass



if __name__ == "__main__":
    nums = [1, 2, 2, 1]
    head = LinkList()
    for num in nums:
        head.append(num)
    print(travel(head.head))
