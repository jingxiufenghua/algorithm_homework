#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode105.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/19 15:10 
'''
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(inorder)
        def dfs(preorder,inorder):
            if not preorder: return None
            root = TreeNode(preorder[0])
            root_index = inorder.index(preorder[0])
            left_tree_inorder = inorder[:root_index]
            right_tree_inorder = inorder[root_index+1:]
            if left_tree_inorder and right_tree_inorder:
                left_tree_preorder = preorder[1:len(left_tree_inorder)+1]
                right_tree_preorder = preorder[1+len(left_tree_inorder):]
            if not left_tree_inorder and not right_tree_inorder:
                left_tree_preorder,right_tree_preorder = [],[]
            elif not left_tree_inorder:
                left_tree_preorder = []
                right_tree_preorder = preorder[1:]
            elif not right_tree_inorder:
                right_tree_preorder = []
                left_tree_preorder = preorder[1:]
            root.left = dfs(left_tree_preorder[:],left_tree_inorder[:])
            root.right = dfs(right_tree_preorder[:],right_tree_inorder[:])
            return root
        return  dfs(preorder,inorder)

node7 = TreeNode(7)
node15 = TreeNode(15)
node20 = TreeNode(20,node7,node15)
node9 = TreeNode(9)
node3 = TreeNode(3,node9,node20)

solution = Solution()
preorder = [3,2,1,4]
inorder = [1,2,3,4]
result = solution.buildTree(preorder,inorder)
print(result)




