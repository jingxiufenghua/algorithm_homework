#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：jianzhi_offer55-II.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/27 22:33 
'''
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root : return True
        def dfs(root,deep):
            if not root : return deep
            deep += 1
            left = dfs(root.left,deep)
            right = dfs(root.right,deep)
            return max(left,right)
        return abs(dfs(root.left,0)-dfs(root.right,0))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1

node3 = TreeNode(3)
node7 = TreeNode(7)
node5 = TreeNode(5,node3,node7)
solution = Solution()
result = solution.isBalanced(node5)
print(result)
