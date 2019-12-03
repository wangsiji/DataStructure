# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 11:35 下午
# @Author  : siJi
# @File    : 203_移除链表元素.py
# @Desc    : 链表

"""
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

