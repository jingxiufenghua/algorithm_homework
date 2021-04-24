#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode563.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/24 0:01 
'''
# 563. 二叉树的坡度
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def dfs(root,val):
            if not root : return 0
            left = dfs(root.left,val)
            right = dfs(root.right,val)
            self.diff += abs(left-right)
            val += left + right + root.val
            return  val
        self.diff = 0
        dfs(root,0)
        return self.diff

