# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 11:38 上午
# @Author  : siJi
# @File    : 面试题53_I_在排序数组中查找数字I.py
# @Desc    :

"""
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8 输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6 输出: 0
 
限制：0 <= 数组长度 <= 50000
"""


class Solution(object):
    def __init__(self):
        self.count = 0

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        方法一 哈希表
        时间复杂度O(n) 空间复杂度O(n)
        '''
        # lookup = {}
        # for num in nums:
        #     lookup[num] = lookup.get(num, 0) + 1
        # return lookup[target] if target in lookup else 0

        '''
        方法二 直接遍历
        时间复杂度O(n) 空间复杂度O(1)
        '''
        # res = 0
        # for num in nums:
        #     if num == target:
        #         res += 1
        # return res
        '''
        方法三 二分查找
        时间复杂度O(logn),空间复杂度O(1)
        '''
        # if not nums:
        #     return 0
        # mid = len(nums) // 2
        # if nums[mid] == target:
        #     self.count += 1
        #     self.search(nums[:mid], target)
        #     self.search(nums[mid+1:], target)
        # elif nums[mid] < target:
        #     self.search(nums[mid+1:], target)
        # else:
        #     self.search(nums[:mid], target)
        # return self.count


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().search(nums, target))
