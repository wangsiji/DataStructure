# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 10:20 上午
# @Author  : siJi
# @File    : 225_用队列实现栈.py
# @Desc    : 栈

"""
使用队列实现栈的下列操作：
push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

注意:
你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        # O(n)
        self.items.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # O(1)
        return self.items.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.items[len(self.items) - 1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.items == []


if __name__ == "__main__":
    s = MyStack()
    print(s.empty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.top())
