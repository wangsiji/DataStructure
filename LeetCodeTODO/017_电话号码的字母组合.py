# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 1:19 下午
# @Author  : siJi
# @File    : 017_电话号码的字母组合.py
# @Desc    : 回溯


"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23" 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明: 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""


"""
回溯是一种通过穷举所有可能情况来找到所有解的算法.
    如果一个候选解最后被发现并不是可行解，回溯算法会舍弃它，并在前面的一些步骤做出一些修改，并重新尝试找到可行解。
    
循环的嵌套层数，就是输入的字符串长度。输入的字符串长度是1，循环只有1层。
输入的字符串长度是3，循环就是3层。如果输入的字符串长度是10，那么循环就是10层。
可是输入的字符串长度是不固定的，对应的循环的嵌套层数也是不固定的，那这种情况怎么解决呢？这时候递归就派上用场了。



"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        '''
        方法一 
        '''
        # res = []
        # if not digits:
        #     return res
        # d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        # def dfs(tmp, index):
        #     # 递归的终止条件, 用index记录每次遍历到字符串的位置
        #     if index == len(digits):
        #         res.append(tmp)
        #         return
        #     # 获取index位置的字符，假设输入的字符是"234"
        #     # 第一次递归时index为0所以c=2，第二次index为1所以c=3，第三次c=4
        #     c = digits[index]
        #     letters = d[ord(c) - ord('0')]
        #     for i in letters:
        #         # 调用下一层递归，用文字很难描述，请配合动态图理解
        #         dfs(tmp + i, index + 1)
        # dfs("", 0)
        # return res

        '''
        方法二 利用队列
        '''
        if not digits:
            return []
        d = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        # 先往队列中加入一个空字符
        res = [""]
        for i in digits:
            size = len(res)
            # 由当前遍历到的字符，取字典表中查找对应的字符串
            letters = d[ord(i) - 48]
            # 计算出队列长度后，将队列中的每个元素挨个拿出来
            for _ in range(size):
                # 每次都从队列中拿出第一个元素
                tmp = res.pop(0)
                # 然后跟"def"这样的字符串拼接，并再次放到队列中
                for j in letters:
                    res.append(tmp + j)
        return res

if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))