# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 2:25 下午
# @Author  : siJi
# @File    : 链表_单向链表.py
# @Desc    : 链表


"""
单向链表也叫单链表，是链表中最简单的一种形式，
它的每个节点包含两个域，一个信息域（元素域）和一个链接域
。这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。


表元素域elem用来存放具体的数据。
链接域next用来存放下一个节点的位置（python中的标识）
变量p指向链表的头节点（首节点）的位置，从p出发能找到表中的任意节点。


is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
"""


class SingleNode(object):
    """节点类"""

    def __init__(self, item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        # = 代表着地址的引用
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node  # 私有属性

    def get_head(self):
        return self.__head

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self.__head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur is not None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        print(self.travel())
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item)
            cur = cur.next
        print("")

    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self.__head
        # 将链表的头_head指向新节点
        self.__head = node

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self.__head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到指定位置
        else:
            print(self.__head)
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur is not None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self.__head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node1, node2 = headA, headB
        while node1 != node2:
            print(node1, node2)
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1

def travel(head):
    """遍历链表"""
    cur = head
    while cur is not None:
        print(cur.item)
        cur = cur.next
    print("")

if __name__ == "__main__":
    ll = SingleLinkList()
    listA = [5, 0, 1, 8, 4, 5]
    listB = [5, 0, 1, 8, 4, 5]
    lA, lB = SingleLinkList(), SingleLinkList()
    for num in listA:
        lA.append(num)
    for num in listB:
        lB.append(num)
    a = lA.get_head()
    b = lB.get_head()
    print(a == b )
    # a = Solution().getIntersectionNode(lA.get_head(), lB.get_head())
    # print(travel(a))