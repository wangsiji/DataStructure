# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 8:29 上午
# @Author  : siJi
# @File    : 560_和为K的子数组.py
# @Desc    :

# TODO
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
        '''
        方法一 暴力
        三次循环
        
        最简单的方法是考虑给定nums 数组的每个可能的子数组，找到每个子数组的元素总和，并检查使用给定 k 获得的总和是否相等。
        当总和等于 k 时，我们可以递增用于存储所需结果的count。
        '''
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         res = 0
        #         for m in range(i, j + 1):
        #             res += nums[m]
        #         if res == k:
        #             count += 1
        # return count

        '''
        方法二 用prefixSum记录前一个总和的状态
        两次循环
        '''
        # count = 0
        # for i in range(len(nums)):
        #     pre_sum = 0
        #     for j in range(i, len(nums)):
        #         pre_sum += nums[j]
        #         if pre_sum == k:
        #             count += 1
        # return count

        '''
        方法三 用prefixSumArray保存prefixSum
        '''
        prefixSumArray = {0: 1}
        count = 0
        prefixSum = 0

        for ele in nums:
            prefixSum += ele
            subArray = prefixSum - k

            if subArray in prefixSumArray:
                count += prefixSumArray[subArray]
            '''
            prefixSumArray.get(prefixSum, 0)
            在hash table里查找key，如果有返回对应的value，反之返回0 
            '''
            prefixSumArray[prefixSum] = prefixSumArray.get(prefixSum, 0) + 1

        return count


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(Solution().subarraySum(nums, k))
