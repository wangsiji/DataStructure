# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 11:53 下午
# @Author  : siJi
# @File    : 栈.py
# @Desc    : 栈


"""
由于栈数据结构只允许在一端进行操作，因而按照后进先出（LIFO, Last In First Out）的原理运作。
"""


class Stack(object):
    """栈"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return not self.items

    def push(self, item):
        """加入元素"""
        self.items.append(item)

    def pop(self):
        """弹出元素"""
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.items[len(self.items) - 1]

    def size(self):
        """返回栈的大小"""
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
