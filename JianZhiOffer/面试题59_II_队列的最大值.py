# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 10:32 下午
# @Author  : siJi
# @File    : 面试题59_II_队列的最大值.py
# @Desc    :

"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：
输入:  ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"] [[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

示例 2：
输入: ["MaxQueue","pop_front","max_value"] [[],[],[]]
输出: [null,-1,-1]
 

限制：
    1 <= push_back,pop_front,max_value的总操作数 <= 10000
    1 <= value <= 10^5
"""
import queue


class MaxQueue:
    """1队列+1双端队列"""

    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1
        # return self.deque[0] if self.deque else -1 或者这样写

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque: return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans


if __name__ == "__main__":
    queue = MaxQueue()
    queue.push_back(1)
    queue.push_back(2)
    print(queue.max_value())
    print(queue.pop_front())
    print(queue.max_value())
