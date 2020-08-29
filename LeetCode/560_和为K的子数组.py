# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 11:37 下午
# @Author  : siJi
# @File    : 560_和为K的子数组.py
# @Desc    : 前缀和+哈希表


"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

说明 :
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        方法一 暴力枚举
        时间复杂度：O(n**2) 空间复杂度：O(1)
        """
        # count = 0
        # for i in range(len(nums)):
        #     s = 0  # 记录当前子数组的和
        #     #  考虑所有0到i的位置作为子数组的开头
        #     for j in range(i, -1, -1):
        #         s += nums[j]
        #         if s == k:
        #             count += 1
        # return count

        """
        方法二 前缀和 + 哈希表优化
        nums 3 4 7  2  -3 1  4  2 
        pre  3 7 14 16 13 14 18 20 
        """
        pre_times = {0: 1}  # 存储某“前缀和”出现的次数,先给定一个初始值，代表前缀和为0的出现了一次
        pre = 0  # 记录到当前位置的前缀和
        res = 0
        for num in nums:
            pre += num
            # 如果前缀和减去目标值k所得到的值在字典中出现，即当前位置前缀和减去之前某一位的前缀和等于目标值
            if pre - k in pre_times:
                res += pre_times[pre - k]
            pre_times[pre] = pre_times.get(pre, 0) + 1
        return res


if __name__ == "__main__":
    nums = [3, 4, 7, 2, -3, 1, 4, 2]
    k = 7
    print(Solution().subarraySum(nums, k))
