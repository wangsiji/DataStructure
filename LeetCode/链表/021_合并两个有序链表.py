# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 9:33 上午
# @Author  : siJi
# @File    : 021_合并两个有序链表.py
# @Desc    : 链表


"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """ 
        递归  
        时间复杂度：O(n+m)O(n+m)。 
            因为每次调用递归都会去掉 l1 或者 l2 的头元素（直到至少有一个链表为空），函数 mergeTwoList 中只会遍历每个元素一次。
            所以，时间复杂度与合并后的链表长度为线性关系。
        空间复杂度：O(n+m)O(n+m)。
            调用 mergeTwoLists 退出时 l1 和 l2 中每个元素都一定已经被遍历过了，所以 n+mn+m 个栈帧会消耗 O(n+m)O(n+m) 的空间。
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
