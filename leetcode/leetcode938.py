#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode938.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/27 22:12 
'''
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(root):
            if not root: return
            if root.val >= low and root.val<=high:
                self.sum += root.val
            dfs(root.left)
            dfs(root.right)
        self.sum = 0
        dfs(root)
        return self.sum
node3 = TreeNode(3)
node7 = TreeNode(7)
node5 = TreeNode(5,node3,node7)
solution = Solution()
result = solution.rangeSumBST(node5,7,15)
print(result)