# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 10:00 上午
# @Author  : siJi
# @File    : 面试题57_II_和为s的连续正数序列.py
# @Desc    : 滑动窗口、数学

"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
输入：target = 9 输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15 输出：[[1,2,3,4,5],[4,5,6],[7,8]] 

限制：1 <= target <= 10^5
"""


class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        '''
        方法一 滑动窗口
            左边界为i，右边界为j
        窗口何时扩大，何时缩小？
            当窗口的和小于 target 的时候，窗口的和需要增加，所以要扩大窗口，窗口的右边界向右移动
            当窗口的和大于 target 的时候，窗口的和需要减少，所以要缩小窗口，窗口的左边界向右移动
            当窗口的和恰好等于 target 的时候，我们需要记录此时的结果。设此时的窗口为[i,j)，那么我们已经找到了一个i 开头的序列，也是唯一一个 i 开头的序列，接下来需要找 i+1 开头的序列，所以窗口的左边界要向右移动
        滑动窗口能找到全部的解吗？
        '''
        # i, j, count = 1, 1, 0  # 滑动窗口的左边界 滑动窗口的右边界 滑动窗口中数字的和
        # res = []
        # while i <= target // 2:
        #     if count < target:
        #         count += j
        #         j += 1
        #     elif count > target:
        #         count -= i
        #         i += 1
        #     else:
        #         tmp = [m for m in range(i, j)]
        #         count -= i
        #         i = i + 1
        #         res.append(tmp)
        # return res
        '''
        方法二 数学
        等差数列 a位首项，1为公差 m为项数 target = ma + (m)(m-1)/2
        ma = target - (m)(m-1)/2
        目标即寻找满足条件的 m、a 对
        '''
        res = []
        for n in range(2, target + 1):
            tmp = target - n * (n - 1) // 2
            if tmp <= 0:
                break
            if not tmp % n:
                a = tmp // n
                res.append([a + i for i in range(n)])
        return res[::-1]


if __name__ == "__main__":
    target = 15
    print(Solution().findContinuousSequence(target))
