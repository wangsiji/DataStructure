# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 8:38 上午
# @Author  : siJi
# @File    : 033_搜索旋转排序数组.py
# @Desc    :


"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 二分查找
        # 旋转后，一边符合升序，一边不符合
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            # 左边生序
            if nums[left] <= nums[mid]:
                # 在左边范围内
                if nums[left] <= target & target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右边生序
            else:
                # 在右边范围内
                if nums[right] >= target & target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(Solution().search(nums, target))
