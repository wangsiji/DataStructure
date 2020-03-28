# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 8:05 下午
# @Author  : siJi
# @File    : 面试题35_复杂链表的复制.py
# @Desc    : DFS BFS 递归 队列


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


# https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/lian-biao-de-shen-kao-bei-by-z1m/
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        '''
        方法一 copy.deepcopy()
        '''
        # import copy
        # return copy.deepcopy(head)

        '''
        方法二 DFS 
            1. 从头结点 head 开始拷贝；
            2. 由于一个结点可能被多个指针指到，因此如果该结点已被拷贝，则不需要重复拷贝；
            3. 如果还没拷贝该结点，则创建一个新的结点进行拷贝，并将拷贝过的结点保存在哈希表中；
            4. 使用递归拷贝所有的 next 结点，再递归拷贝所有的 random 结点。
        '''

        def dfs(head):
            if not head:
                return None
            if head in visited:
                return visited[head]
            # 创建新节点
            copy = Node(head.val)
            visited[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(copy.random)
            return copy

        visited = {}
        return dfs(head)

        '''
        方法二 O(1)
        时间复杂度：O(n) 空间复杂度：O(1)
        '''
        # if not head:
        #     return None
        # prev = head
        # # 遍历原来的链表并拷贝每一个节点，将拷贝节点放在原来节点的旁边，创造出一个旧节点和新节点交错的链表。
        # # A->B A->A'->B->B'
        # while prev:
        #     new_node = Node(prev.val)  # 新节点
        #     new_node.next = prev.next  # A'->B
        #     prev.next = new_node  # A->A'
        #     prev = new_node.next  # B
        # # 修改每个新结点的 next 指针和 random 指针。
        # # A->B A->A'->B->B'
        # prev = head
        # while prev:
        #     next_origin = prev.next.next  # 下一个旧节点 B
        #     prev.next.next = next_origin.next if not next_origin else None  # 修改新结点的next A'->B'
        #     prev.next.random = prev.random.next if not prev.random else None  # 修改新结点的 random
        #     prev = next_origin  # B
        # return head.next


if __name__ == "__main__":
    pass
