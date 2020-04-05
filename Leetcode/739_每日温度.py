# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 3:55 下午
# @Author  : siJi
# @File    : 739_每日温度.py
# @Desc    : 栈

"""
根据每日气温列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。
如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        """
        方法一 暴力解法 向后进行依次搜索
        """
        # res = []
        # for i in range(len(T) - 1):
        #     day = i + 1
        #     while day < len(T) and T[day] <= T[i]:
        #         day += 1
        #     day_diff = day - i if day < len(T) else 0
        #     res.append(day_diff)
        # res.append(0)
        # return res

        """
        方法二 栈
        递减栈 ：栈里只有递减元素。
        
        遍历整个数组
            如果栈不空，且当前数字大于栈顶元素，那么如果直接入栈的话就不是递减栈 ，所以需要取出栈顶元素，
                由于当前数字大于栈顶元素的数字，而且一定是第一个大于栈顶元素的数，直接求出下标差就是二者的距离。
        """
        res = [0 for _ in range(len(T))]
        stack = []
        for index, value in enumerate(T):
            while stack and value > T[stack[-1]]:
                res[stack.pop()] = index - stack[-1]
            stack.append(index)
        return res


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temperatures))
