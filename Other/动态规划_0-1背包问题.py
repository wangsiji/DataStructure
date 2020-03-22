# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 2:48 上午
# @Author  : siJi
# @File    : 动态规划_0-1背包问题.py
# @Desc    : 动态规划
import numpy as np

def knapsack(w, v, C):
    mem = np.zeros((len(w) + 1, C + 1))
    for i in range(1, len(w) + 1):
        for j in range(1, C + 1):
            if w[i - 1] <= j:
                mem[i, j] = max(mem[i - 1, j], mem[i - 1, j - w[i - 1]] + v[i - 1])
            else:
                mem[i, j] = mem[i - 1, j]
    return mem


if __name__ == "__main__":
    w = [4, 6, 2, 2, 5, 1]
    v = [8, 10, 6, 3, 7, 2]
    C = 12
    print(knapsack(w, v, C))
