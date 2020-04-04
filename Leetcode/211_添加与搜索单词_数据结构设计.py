# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 11:01 下午
# @Author  : siJi
# @File    : 211_添加与搜索单词_数据结构设计.py
# @Desc    :

"""
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.word_dict = defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.word_dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        for item in self.word_dict[len(word)]:
            flag = False
            for x, y in zip(item, word):
                if y == "." or x == y:
                    continue
                else:
                    flag = True
                    break
            if not flag:
                return True
        return False


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.word_dict)
    print(wd.search("pad"))  # false
    print(wd.search("bad"))  # true
    print(wd.search(".ad"))  # true
    print(wd.search("b.."))  # true
