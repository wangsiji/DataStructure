# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 9:58 上午
# @Author  : siJi
# @File    : 数组中两个数相减(相加)的最大值.py
# @Desc    :

"""
有一个数组，找出数组中前面的数减去后面的数的最大值。例如数组{9,1,7,18,3,-2,20,4,0,5}，最大值是18-（-2）或者20-0。
"""


class Solution(object):
    def max_minus(self, nums):
        """
        时间复杂度O(n),空间复杂度O(1).

        EX:
            nums [9, 1, 7, 18, 3, -2, 20, 4, 0, 5]
            left=9  right=1 res=8  left=9  right=7 res=2
            left=18 right=3 res=15 left=18 right=3 res=15 left=18 right=-2 res=20
            left=20 right=4 res=16 left=20 right=0 res=20 left=20 right=5 res=15
        """
        if len(nums) == 0 or len(nums) == 1:
            return 0
        if len(nums) == 2:
            return
        left, right = 0, 1
        res = nums[left] - nums[right]
        while right < len(nums):
            while right < len(nums) and nums[right] < nums[left]:
                res = max(res, nums[left] - nums[right])
                right += 1
            left = right
            right += 1
        return res


if __name__ == "__main__":
    nums = [9, 1, 7, 18, 3, -2, 20, 4, 0, 5]
    print(Solution().max_minus(nums))
