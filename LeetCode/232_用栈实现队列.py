# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 10:21 上午
# @Author  : siJi
# @File    : 232_用栈实现队列.py
# @Desc    : 队列

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # O(n)
        self.items.insert(0, x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.items.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.items[len(self.items) - 1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.items == []
