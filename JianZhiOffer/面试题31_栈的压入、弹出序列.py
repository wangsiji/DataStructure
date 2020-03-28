# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 10:18 下午
# @Author  : siJi
# @File    : 面试题31_栈的压入、弹出序列.py
# @Desc    :

"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

示例 1：
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1] 输出：true
解释：我们可以按以下顺序执行：
    push(1), push(2), push(3), push(4), pop() -> 4,
    push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

示例 2：
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2] 输出：false
解释：1 不能在 2 之前弹出。
 
提示：
    0 <= pushed.length == popped.length <= 1000
    0 <= pushed[i], popped[i] < 1000
    pushed 是 popped 的排列。
"""


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        '''
        方法一 贪心算法 
        所有的元素一定是按顺序 push 进去的，重要的是怎么 pop 出来？
        
        将 pushed 队列中的每个数都 push 到栈中，同时检查这个数是不是 popped 序列中下一个要 pop 的值，如果是就把它 pop 出来。
        最后，检查不是所有的该 pop 出来的值都是 pop 出来了。
        '''
        j =  0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)


if __name__ == "__main__":
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    print(Solution().validateStackSequences(pushed, popped))
