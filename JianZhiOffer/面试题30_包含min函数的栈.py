# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 6:58 下午
# @Author  : siJi
# @File    : 面试题30_包含min函数的栈.py
# @Desc    : 辅助栈

"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();   --> 返回 0.
minStack.min();   --> 返回 -2.

提示：各函数的调用总次数不超过 20000 次
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

    def min(self):
        """
        :rtype: int
        """
        return self.stack_b[-1]


if __name__ == "__main__":
    minStack = MinStack()
