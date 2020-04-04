# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 9:26 下午
# @Author  : siJi
# @File    : 006_Z字形变换.py
# @Desc    :

"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：string convert(string s, int numRows);

示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3 输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4 输出: "LDREOEIIECIHNTSG"

解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""

"""
字符串s是以Z字形为顺序存储的字符串，目标是按行打印。
设numRows行字符串分别为s1,s2,...,sn，则容易发现：按顺序遍历字符串s时，每个字符c在Z字形中对应的行索引先从s1增大至sn，再从sn减小至s1……如此反复。
因此，解决方案为：模拟这个行索引的变化，在遍历s中把每个字符填到正确的行res[i]。
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """时间复杂度:O(N),空间复杂度:O(N)"""
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)


if __name__ == "__main__":
    s = "LEETCODEISHIRING"
    numRows = 4
    print(Solution().convert(s, numRows))
