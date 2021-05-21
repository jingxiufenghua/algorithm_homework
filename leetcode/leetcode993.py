#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode993.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/17 10:01 
'''
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(root,target,i,pre,save):
            if not root : return
            if root.val == target:
                save.append([i,pre])
                return save
            dfs(root.left,target,i+1,root,save)
            dfs(root.right,target,i+1,root,save)
        x_info , y_info = [],[]
        dfs(root,x,0,None,x_info)
        dfs(root,y,0,None,y_info)
        print(x_info,y_info)
        if x_info[0][0] == y_info[0][0] and x_info[0][1]!=y_info[0][1]:
            return True
        return False

node4 = TreeNode(4)
node2 = TreeNode(2,None,node4)
node5 = TreeNode(5)
node3 = TreeNode(3,None,node5)
root = TreeNode(1,node2,node3)
solution = Solution()
result = solution.isCousins(root,4,5)
print(result)
