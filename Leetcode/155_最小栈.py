# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 3:51 下午
# @Author  : siJi
# @File    : 155_最小栈.py
# @Desc    : 栈

"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
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


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_a, self.stack_b = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_a.append(x)
        # 位空 栈最上面的大于等于
        if not self.stack_b or self.stack_b[-1] >= x:
            self.stack_b.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack_a.pop() == self.stack_b[-1]:
            self.stack_b.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack_a[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_b[-1]