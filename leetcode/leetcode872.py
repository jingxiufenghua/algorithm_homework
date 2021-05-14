#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode872.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/10 15:42 
'''
from typing import List
# 872. 叶子相似的树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2 : return True
        if not root1 or not root2 : return False
        def dfs(root,nums):
            if not root: return
            if not root.left and not root.right :
                nums.append(root.val)
                return
            dfs(root.left,nums)
            dfs(root.right,nums)
        nums1,nums2 = [],[]
        dfs(root1,nums1)
        dfs(root2,nums2)
        return nums1 == nums2
