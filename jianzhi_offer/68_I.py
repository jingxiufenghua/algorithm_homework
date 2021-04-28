#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：68_I.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/28 19:03 
'''
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':




