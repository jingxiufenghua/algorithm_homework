#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode897.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/25 10:28 
'''
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def increasingBST(self, root: TreeNode) -> TreeNode:
    #     def dfs(root):
    #         if not root: return
    #         dfs(root.left)
    #         res.append(root)
    #         dfs(root.right)
    #     res = []
    #     dfs(root)
    #     print(res)
    #     ans = tree = TreeNode()
    #     for node in res:
    #         tree.right = TreeNode(node.val)
    #         tree = tree.right
    #     return ans.right

    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root: return
            inorder(root.left)
            self.tree.right = root
            root.left = None
            self.tree = root
            inorder(root.right)
        self.tree = ans = TreeNode(-1)
        inorder(root)
        return ans.right

leaf1 = TreeNode(1)
leaf3 = TreeNode(3)
leaf4 = TreeNode(4,leaf3,None)
leaf2 = TreeNode(2,leaf1,leaf4)
solution = Solution()
result = solution.increasingBST(leaf2)
print(result)



