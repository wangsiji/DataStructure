# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 5:11 下午
# @Author  : siJi
# @File    : 面试题13_机器人的运动范围.py
# @Desc    :


"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？


示例 1：
输入：m = 2, n = 3, k = 1 输出：3

示例 1：
输入：m = 3, n = 1, k = 0 输出：1

提示：
1 <= n,m <= 100 0 <= k <= 20
"""


def sums(x):
    s = 0
    while x:
        s += x % 10
        x = x // 10
    return s


class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        '''
        方法一 DFS
        深度优先搜索： 可以理解为暴力法模拟机器人在矩阵中的所有路径。DFS 通过递归，先朝一个方向搜到底，再回溯至上个节点，沿另一个方向搜索，以此类推。
        剪枝： 在搜索中，遇到数位和超出目标值、此元素已访问，则应立即返回，称之为 可行性剪枝 
        
        数位和增量公式：x的数位和为sx, x+1的数位和为s1
            （x+1）% 10 = 0 => s1 = sx-8  例如 19 20 => 10 2
            （x+1）% 10 != 0 => s1 = sx+1 例如 2  1  => 2  1
            ==> s_x + 1 if (x + 1) % 10 else s_x - 8
            
        算法解析：
            递归参数： 当前元素在矩阵中的行列索引 i 和 j ，两者的数位和 si, sj 。
            终止条件： 当 ① 行列索引越界 或 ② 数位和超出目标值 k 或 ③ 当前元素已访问过 时，返回0,代表不计入可达解。
            递推工作：
                标记当前单元格 ：将索引 (i, j) 存入 Set visited 中，代表此单元格已被访问过。
                搜索下一单元格： 计算当前元素的 下、右 两个方向元素的数位和，并开启下层递归 。
            回溯返回值： 返回 1 + 右方搜索的可达解总数 + 下方搜索的可达解总数，代表从本单元格递归搜索的可达解总数。
        时间复杂度：O(mn) 空间复杂度：O(mn)
        
        '''
        # visited = set()
        #
        # def dfs(i, j, si, sj):
        #     if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited:
        #         return 0
        #     visited.add((i, j))
        #
        #     return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si,
        #                                                                            sj + 1 if (j + 1) % 10 else sj - 8)
        #
        # return dfs(0, 0, 0, 0)

        '''
        方法二 BFS
        BFS/DFS ： 两者目标都是遍历整个矩阵，不同点在于搜索顺序不同。DFS 是朝一个方向走到底，再回退，以此类推；BFS 则是按照“平推”的方式向前搜索。
        BFS 实现： 通常利用队列实现广度优先遍历。
        '''
        queue, visited = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if not 0 <= i < m or not 0 <= j < n or si + sj > k or (i, j) in visited:
                continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)


if __name__ == "__main__":
    m = 20
    n = 20
    k = 6
    print(Solution().movingCount(m, n, k))
