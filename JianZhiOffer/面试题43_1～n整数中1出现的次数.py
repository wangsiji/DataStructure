# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 5:48 下午
# @Author  : siJi
# @File    : 面试题43_1～n整数中1出现的次数.py
# @Desc    :

"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：
输入：n = 12 输出：5

示例 2：
输入：n = 13 输出：6

限制：1 <= n < 2^31
"""


# TODO
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        方法一 暴力法
        '''
        # res = 0
        # for i in range(1, n + 1):
        #     for s in str(i):
        #         if s == "1":
        #             res += 1
        # return res

        '''
        方法二 数学
        每10个数，个位上的’1’ 就会出现一次。同样的，每100 个数，十位上的’1’ 就会出现十次
        1234 
            非最高位：
                个位 1234//10 * 1  + min(1234%10, 1) = 124
                十位 1234//100 * 10 + min(1234%100, 10) = 130
                百位 1234//1000 * 100 + min(1234%1000, 100) = 200
            最高位：
                千位 min(1234%1000+1=235, 1000)
        20
            非最高位：
                个位 20//10 * 1  + min(0, 1) = 2
            最高位：
                十位 min(20%10+1, )
        101 
            个位 101//10 * 1  + min(101%10, 1) = 11
            十位 101//100 * 10 + min(101%100, 10) = 11
            百位 1234//1000 * 100 + min(1234%1000, 100) = 200
        '''
        res = 0
        if not n:
            return res
        for i in range(len(str(n))):
            if i != len(str(n)) - 1:
                position = 10 ** i  # 个位、十位、百位
                count = n // (position * 10) * position + min(n % (position * 10), position)

                print(count)
                # print(n // (10 ** (i + 1)) * (10 ** i) + min(n % (10 ** (i + 1)), 10 ** i))
                #
                # res += n // (10 ** (i + 1)) * (10 ** i) + min(n % (10 ** (i + 1)), 10 ** i)
            else:
                if str(n)[0] == "1":
                    count = n % (10 ** i) + 1
                else:
                    count = 10 ** i
                print(count)
        return res


if __name__ == "__main__":
    print(Solution().countDigitOne(101))
