# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 11:48 下午
# @Author  : siJi
# @File    : 155_最小栈.py
# @Desc    : 栈

"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""

"""
以空间换时间，使用辅助栈是常见的做法。
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[len(self.items) - 1]

    def getMin(self):
        """
        :rtype: int
        """


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    obj.top()
    print(obj.getMin())
