#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1026.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/19 17:05 
'''
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import numpy as np
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(root,max_value,min_value):
            if not root : return max_value,min_value
            max_value = max(max_value,root.val)
            min_value = min(min_value,root.val)
            left_max_value,left_min_value = dfs(root.left,max_value,min_value)
            right_max_value,right_min_value = dfs(root.left,max_value,min_value)
            return max(max_value,max(left_max_value,right_max_value)),min(min_value,min(left_min_value,right_min_value))
        max_return,min_return = dfs(root,-2**31,2**31-1)
        return 0
node13 = TreeNode(13)
node14 = TreeNode(14,node13)
node10 = TreeNode(10,None,node14)
node4 = TreeNode(4)
node7 = TreeNode(7)
node6 = TreeNode(6,node4,node7)
node1 = TreeNode(1)
node3 = TreeNode(3,node1,node6)
node8 = TreeNode(8,node3,node10)
solution = Solution()
result = solution.maxAncestorDiff(node8)
print(result)

