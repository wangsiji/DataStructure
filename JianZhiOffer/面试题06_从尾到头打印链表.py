# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 9:54 下午
# @Author  : siJi
# @File    : 面试题06_从尾到头打印链表.py
# @Desc    : 链表

"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""


class ListNode:
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


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        """
        方法一  用辅助栈存储
        """
        # stack = []
        # res = []
        # while listNode:
        #     stack.append(listNode.val)
        #     listNode = listNode.next
        # while stack:
        #     res.append(stack.pop())
        # return res

        """
        方法二 递归
        """
        if not listNode:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]


if __name__ == "__main__":
    nums = [1, 2, 3]
    head = LinkList()
    for num in nums:
        head.append(num)
    print(Solution().printListFromTailToHead(head.head))
