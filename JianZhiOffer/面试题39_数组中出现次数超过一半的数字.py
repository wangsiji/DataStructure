# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 12:15 下午
# @Author  : siJi
# @File    : 面试题39_数组中出现次数超过一半的数字.py
# @Desc    : 摩尔投票法


"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:输入: [1, 2, 3, 2, 2, 2, 5, 4, 2] 输出: 2
 
限制：1 <= 数组长度 <= 50000
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        方法一 哈希表
        时间复杂度：O(n) 空间复杂度：O(n)
        '''
        # import collections
        # counts = collections.Counter(nums)
        # res = max(counts.keys(), key=counts.get)
        # return res
        '''
        方法二 排序
        '''
        # return sorted(nums)[len(nums) // 2]
        '''
        方法三 摩尔投票法  核心理念为 “正负抵消” 。
        时间复杂度为 O(N) ，空间复杂度为 O(1)
        
        如果我们把众数记为+1，把其他数记为−1，将它们全部加起来，显然和大于0，从结果本身我们可以看出众数比其他数多。
        
        投票算法证明：
            如果候选人不是maj 则 maj,会和其他非候选人一起反对 候选人,所以候选人一定会下台
            如果候选人是maj , 则maj 会支持自己，其他候选人会反对，同样因为maj 票数超过一半，所以maj 一定会成功当选
        '''
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x


if __name__ == "__main__":
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(Solution().majorityElement(nums))
