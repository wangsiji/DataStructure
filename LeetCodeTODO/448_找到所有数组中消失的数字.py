# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 4:15 下午
# @Author  : siJi
# @File    : 448_找到所有数组中消失的数字.py
# @Desc    :

"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
示例:
输入: [4,3,2,7,8,2,3,1]
输出: [5,6]
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        方法一 哈希表
        时间复杂度：O(n)
        空间复杂度：O(n)
        '''
        # import collections
        # res = []
        # count = collections.Counter(nums)
        # for i in range(1, len(nums)+1):
        #     if i not in count:
        #         res.append(i)
        # return res

        '''
        方法二 原地修改
            遍历输入数组的每个元素一次。
            我们将把 |nums[i]|-1 索引位置的元素标记为负数。即nums[∣nums[i]∣−1]×−1 。
            然后遍历数组，若当前数组元素 nums[i] 为负数，说明我们在数组中存在数字 i+1。
        '''
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        result = []
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
        return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(nums))
