# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 8:05 下午
# @Author  : siJi
# @File    : 面试题35_复杂链表的复制.py
# @Desc    :


"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

提示：
    -10000 <= Node.val <= 10000
    Node.random 为空（null）或指向链表中的节点。
    节点数目不超过 1000 。
"""


"""
浅拷贝只复制指向某个对象的指针，而不复制对象本身，新旧对象还是共享同一块内存。
但深拷贝会另外创造一个一模一样的对象，新对象跟原对象不共享内存，修改新对象不会改到原对象。
对于简单的 object，用 shallow copy 和 deep copy 没区别
"""
# TODO
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, hezad):
        """
        :type head: Node
        :rtype: Node
        """
        '''
        方法一 copy.deepcopy()
        '''
        # import copy
        # return copy.deepcopy(head)


if __name__ == "__main__":
    pass
