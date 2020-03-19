# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 7:03 下午
# @Author  : siJi
# @File    : 面试题24_反转链表.py
# @Desc    :

"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL
 
限制：0 <= 节点个数 <= 5000
"""
# TODO

# Definition for singly-linked list.
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

    def get_head(self):
        return self.head


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        双指针
        定义两个指针：pre 和 cur ；pre 在前 cur 在后。
        每次让 pre 的 next 指向 cur ，实现一次局部反转完成之后， 
        pre 和 cur 同时往前移动一个位置
        循环上述过程，直至 pre 到达链表尾部
        '''
        latter, former = None, head
        while former:
            temp = former.next
            former.next = latter
            latter, former = former, temp
        return latter

    def travel(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next
        print("")


if __name__ == "__main__":
    ll = LinkList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    head = ll.get_head()

    # print(Solution().reverseList(head))
    print(Solution().travel(head))
