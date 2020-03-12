# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 6:23 下午
# @Author  : siJi
# @File    : 面试题11_旋转数组的最小数字.py
# @Desc    : 二分查找

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：
输入：[3,4,5,1,2] 输出：1

示例 2：
输入：[2,2,2,0,1] 输出：0
"""


class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        """
        二分查找
        [3,4,5,1,2,3]
        left mid right
        numbers[mid] > numbers[right] mid一定在左排序数组中, 旋转点x一定在[m+1, right]
        numbers[mid] < numbers[right] mid一定在右排序数组中, 旋转点x一定在[left, m]
        numbers[mid] = numbers[right] 
        """
        left, right = 0, len(numbers)-1
        while left < right:
            mid = left + (right - left) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1  # 转折点在右边
            elif numbers[mid] < numbers[right]:
                right = mid  # 转折点在左边
            else:
                right -= 1
        return numbers[left]


if __name__ == "__main__":
    numbers = [3, 4, 5, 1, 2]
    print(Solution().minArray(numbers))
