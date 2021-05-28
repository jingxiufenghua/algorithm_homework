#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework
@File    ：leetcode98.py
@IDE     ：PyCharm
@Author  ：无名
@Date    ：2021/5/22 12:39 
'''
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root,lower=float("-inf"),upper=float("inf")):
            if not root : return True
            val = root.val
            if val<=lower or val>=upper:
                return False
            if not dfs(root.right,val,upper):
                return False
            if not dfs(root.left,lower,val):
                return False
            return True
        return dfs(root)


