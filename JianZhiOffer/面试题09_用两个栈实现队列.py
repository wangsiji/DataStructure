# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 6:04 下午
# @Author  : siJi
# @File    : 面试题09_用两个栈实现队列.py
# @Desc    : 辅助栈


"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。
(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：
输入：["CQueue","appendTail","deleteHead","deleteHead"] [[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"] [[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

提示： 1 <= values <= 10000 最多会对 appendTail、deleteHead 进行 10000 次调用
"""

"""
对于入栈，我们使用append， 即往尾部插入一个元素。
对于出栈，我们使用pop(-1)，即删除尾部的元素
"""


class CQueue(object):

    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack_a.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        """
        方法一 暴力解法
        """
        # while self.stack_a:
        #     self.stack_b.append(self.stack_a.pop())
        # res = self.stack_b.pop() if self.stack_b else -1
        # while self.stack_b:
        #     self.stack_a.append(self.stack_b.pop())
        # return res
        """
        方法二 优化
        """
        if not self.stack_b:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop() if self.stack_b else -1


if __name__ == "__main__":
    queue = CQueue()
    print(queue.appendTail(3))
    print(queue.deleteHead())
