# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 12:14 下午
# @Author  : siJi
# @File    : 面试题07_重建二叉树.py
# @Desc    : 树 、递归

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
    返回如下的二叉树：

        3
       / \
      9  20
        /  \
       15   7
 
限制：0 <= 节点个数 <= 5000
"""

"""
https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/mian-shi-ti-07-zhong-jian-er-cha-shu-di-gui-fa-qin/

前序遍历 preorder = [3|9|20 15 7]
中序遍历 inorder =  [9|3|15 20 7]

[20|15|7]
[15|20|7]
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, x):
        pass


class Solution(object):

    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right: return  # 终止条件：中序遍历为空
        root = TreeNode(self.po[pre_root])  # 建立当前子树的根节点
        i = self.dic[self.po[pre_root]]  # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树完成划分。
        root.left = self.recur(pre_root + 1, in_left, i - 1)  # 开启左子树的下层递归
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right)  # 开启右子树的下层递归
        return root  # 返回根节点，作为上层递归的左（右）子节点

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        '''
        递归：
            递推参数： 前序遍历中根节点的索引pre_root、中序遍历左边界in_left、中序遍历右边界in_right。
        '''

        def helper(in_left=0, in_right=len(inorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None
            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            # root splits inorder list
            index = idx_map[root_val]
            # recursion
            pre_idx += 1
            # left
            root.left = helper(in_left, index)
            # right
            root.right = helper(index + 1, in_right)
            return root

        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        return helper()


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(Solution().buildTree(preorder, inorder))
