# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 10:59 上午
# @Author  : siJi
# @File    : 007_整数反转.py
# @Desc    : 数学

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123 输出: 321
 
示例 2:
输入: -123 输出: -321

示例 3:
输入: 120 输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = -1 if x < 0 else 1
        p = abs(x)
        res = 0
        # 溢出条件有两个，一个是大于整数最大值MAX_VALUE 2147483647
        # 另一个是小于整数最小值MIN_VALUE  -2147483648
        while p:
            pop = p % 10
            # 最大值溢出
            if flag == 1:
                # 当出现 res > MAX_VALUE / 10 且 还有pop需要添加 时，则一定溢出
                # 当出现 res == MAX_VALUE / 10 且 pop > 7 时，则一定溢出，7是2^31 - 1的个位数
                if (res > (2 ** 31 - 1) / 10) or (res == (2 ** 31 - 1) / 10 and pop > 7):
                    return 0
            # 最小值溢出
            else:
                # 当出现 res > MAX_VALUE / 10 且 还有pop需要添加 时，则一定溢出
                # 当出现 res == MAX_VALUE / 10 且 pop > 7 时，则一定溢出，7是2^31 - 1的个位数
                if (res > 2 ** 31 / 10) or (res == 2 ** 31 / 10 and pop > 8):
                    return 0
            res = res * 10 + pop
            p = p // 10
        return flag * res


if __name__ == "__main__":
    x = 1463847412
    print(Solution().reverse(x))
