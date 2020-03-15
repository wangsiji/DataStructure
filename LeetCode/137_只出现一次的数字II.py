# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 1:37 下午
# @Author  : siJi
# @File    : 137_只出现一次的数字II.py
# @Desc    :

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,3,2] 输出: 3

示例 2:
输入: [0,1,0,1,0,1,99] 输出: 99
"""
# TODO

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        方法一 HashSet
        '''
        # res = 3 * sum(set(nums)) - sum(nums)
        # return res // 2
        '''
        方法二 位运算符
        时间复杂度：O(N)，遍历输入数组
        空间复杂度：O(1)，不使用额外空间
        
        位运算：
            <<	按位左移，左移n位相当于乘以2的n次方
            >>	按位右移 ，左移n位相当于除以2的n次方
            &	按位与，二进制位数同且为1结果位为1
            |	按位或 ，二进制位数或有1结果位为1
            ^	按位异或 ，二进制位数不同结果位为1
            ~	按位取反，二进制位0和1结果位互换
        '''
        seen_once = seen_twice = 0  # 区分出现一次的数字和出现三次的数字，使用两个位掩
        # 位掩码seen_once 仅保留出现一次的数字，不保留出现三次的数字。



if __name__ == "__main__":
    nums = [0, 1, 0, 1, 0, 1, 99]
    print(Solution().singleNumber(nums))
