# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 11:07 上午
# @Author  : siJi
# @File    : 141_环形链表.py
# @Desc    :

"""
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：
输入：head = [3,2,0,-4], pos = 1 输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0 输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：
输入：head = [1], pos = -1 输出：false
解释：链表中没有环。

进阶：你能用 O(1)（即，常量）内存解决此问题吗？
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



class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        方法一 集合
        通过检查一个结点此前是否被访问过来判断链表是否为环形链表
        '''
        # lookup = set()
        # while head:
        #     if head in lookup:
        #         return True
        #     else:
        #         lookup.add(head)
        #     head = head.next
        # return  False
        '''
        方法二：双指针
            使用具有 不同速度 的快、慢两个指针遍历链表，空间复杂度可以被降低至 O(1)
            慢指针每次移动一步，而快指针每次移动两步。
        '''
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return  False
            slow, fast = slow.next, fast.next.next
        return True

