#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：mianshi_101.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/4 23:58 
'''
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L,R):
            if not L and not R : return True
            if not L or not R or(L.val!= R.val):
                return False
            return recur(L.left,R.right) and recur(L.right,R.left)
        return recur(root.left,root.right) if root else True
