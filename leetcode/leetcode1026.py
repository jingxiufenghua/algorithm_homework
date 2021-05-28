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
# class Solution:
#     def maxAncestorDiff(self, root: TreeNode) -> int:
#         def dfs(root,max_value,min_value):
#             if not root : return max_value,min_value
#             max_value = max(max_value,root.val)
#             min_value = min(min_value,root.val)
#             left_max_value,left_min_value = dfs(root.left,max_value,min_value)
#             right_max_value,right_min_value = dfs(root.right,max_value,min_value)
#             return max(max_value,max(left_max_value,right_max_value)),min(min_value,min(left_min_value,right_min_value))
#         left_max_return,left_min_return = dfs(root.left,-2**31,2**31-1)
#         right_max_return,right_min_return = dfs(root.right,-2**31,2**31-1)
#         print(left_max_return,left_min_return)
#         print(right_max_return,right_min_return)
#         ans = []
#         if left_max_return!=-2**31 and left_min_return!=2**31-1:
#             ans.append(abs(left_max_return-left_min_return))
#             ans.append(abs(left_max_return-root.val))
#             ans.append(abs(left_min_return-root.val))
#         if right_max_return!=-2**31 and right_min_return!=2**31-1:
#             ans.append(abs(right_max_return-root.val))
#             ans.append(abs(right_min_return-root.val))
#             ans.append(abs(right_min_return-right_max_return))
#         print(ans)
#         return max(ans)

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.maxvalue = 0
        def dfs(root,maxv,minv):
            if not root:
                self.maxvalue = max(maxv-minv,self.maxvalue)
            else:
                maxv,minv = max(maxv,root.val),min(minv,root.val)
                dfs(root.left,maxv,minv)
                dfs(root.right,maxv,minv)
        dfs(root,0,10001)
        return self.maxvalue



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

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_value = 0
        def dfs(root,maxv,minv):
            if not root:
                self.max_value = max(self.max_value,maxv-minv)
            else:
                maxv = max(maxv,root.val)
                minv = min(minv,root.val)
                dfs(root.left,maxv,minv)
                dfs(root.right,maxv,minv)
        dfs(root,float("-inf"),float("inf"))
        return self.max_value


select *
from
(select *,row_number() over(partition by xxx order by xx desc) as n
from xxxx) a
where a.n<=3
