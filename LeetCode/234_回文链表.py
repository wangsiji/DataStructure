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
        时间复杂度：O(n)
        空间复杂度：O(n)
        '''
        # vals = []
        # cur = head
        # while cur:
        #     vals.append(cur.val)
        #     cur = cur.next
        # return vals == vals[::-1]


        '''
        方法二 快慢指针
        慢指针一次走一步，快指针一次走两步，快慢指针同时出发。
        当快指针移动到链表的末尾时，慢指针到链表的中间。通过慢指针将链表分为两部分。
        '''
        if not head or not head.next:
            return True
        p = ListNode(0)
        p.next, slow, fast = head, p , p
        # 1、找到链表的中点，链表长度奇偶不影响
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur, pre = slow.next, None
        slow.next = None
        # 2、将slow之后链表进行断开且反转，最后翻转完成之后pre指向反转链表的头节点
        while cur:
            cur.next, pre ,cur = pre, cur, cur.next
        a, b = p.next, pre
        while b:
            if a.val != b.val:
                return  False
            a, b = a.next, b.next
        return True



if __name__ == "__main__":
    nums = [1, 2, 3, 2, 1]
    head = LinkList()
    for num in nums:
        head.append(num)
    print(Solution().isPalindrome(head.head))
