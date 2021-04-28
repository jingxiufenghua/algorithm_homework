#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode235.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/28 19:21 
'''
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        while True:
            if p.val<ancestor.val and q.val<ancestor.val:
                ancestor = ancestor.left
            elif p.val>ancestor.val and q.val>ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor
