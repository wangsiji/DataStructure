# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 8:47 上午
# @Author  : siJi
# @File    : 堆.py
# @Desc    :


class Heap(object):
    def __init__(self):
        """
        初始化一个空堆，使用数组来存放堆元素， 节省存储
        """
        self.data_list = []

    def get_parent_index(self, index):
        """
        返回父节点的下标
        """
        if not index:
            return None
        else:
            return (index - 1) >> 1

    def insert(self, data):
        """
        先把元素放在最后，然后从后往前依次堆化
        这里以大顶堆为例，如果插入元素比父节点大，则交换，直到最后
        """
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        # 循环，直到该元素成为堆顶，或小于父节点（对于大顶堆)
        while parent is not None and self.data_list[parent] < self.data_list[index]:
            # 交换数组中两个元素
            self.data_list[parent], self.data_list[index] = self.data_list[index], self.data_list[parent]
            index, parent = parent, self.get_parent_index(parent)

    def remove_max(self):
        """
        删除堆顶元素，然后将最后一个元素放在堆顶，再从上往下依次堆化
        """
        remove_data = self.data_list[0]
        self.data_list[0], self.data_list[-1] = self.data_list[-1], self.data_list[0]
        del self.data_list[-1]
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        """
        从上往下堆化，从index 开始堆化操作 (大顶堆)
        """
        total_index = len(self.data_list) - 1
        while True:
            max_value_index = index
            # 左节点
            if 2 * index + 1 <= total_index and self.data_list[2 * index + 1] > self.data_list[max_value_index]:
                max_value_index = 2 * index + 1
            # 右节点
            if 2 * index + 2 <= total_index and self.data_list[2 * index + 2] > self.data_list[max_value_index]:
                max_value_index = 2 * index + 1
            if max_value_index == index:
                break
            self.data_list[index], self.data_list[max_value_index] = self.data_list[max_value_index], self.data_list[
                index]
            index = max_value_index


if __name__ == "__main__":
    heap = Heap()
    for i in range(5):
        heap.insert(i + 1)
    print("建堆:", heap.data_list)
    print("删除堆顶元素:", [heap.remove_max() for _ in range(5)])
