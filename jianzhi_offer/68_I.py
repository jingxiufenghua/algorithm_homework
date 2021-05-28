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
        def getPath(root:TreeNode,target:TreeNode,path):
            if not root:return
            path.append(root)
            if root == target :
                return path
            if root.val<target.val:
                right = getPath(root.right,target,path)
            else:
                left = getPath(root.left,target,path)
            return path
        path_p = getPath(root,p,[])
        path_q = getPath(root,q,[])
        ancestor = None
        for k,v in zip(path_p,path_q):
            if k == v:
                ancestor = k
            else:
                break
        return ancestor

node1 = TreeNode(1)
node2 = TreeNode(2)
node2.left = node1
solution = Solution()
result = solution.lowestCommonAncestor(node2,node2,node1)
print(result)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getPath(root:TreeNode,target:TreeNode):
            path = []
            node = root
            while node!=target:
                path.append(node)
                if target.val<node.val:
                    node = node.left
                else:
                    node = node.right
            path.append(node)
            return path
        path_p = getPath(root,p)
        path_q = getPath(root,q)
        ancestor = None
        for k,v in zip(path_p,path_q):
            if k == v:
                ancestor = k
            else:
                break
        return ancestor



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if p.val<ancestor.val and q.val<ancestor.val:
                ancestor = ancestor.left
            elif p.val>ancestor.val and q.val>ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor



























class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root,target,path):
            if not root: return
            path.append(root)
            if root.val == target.val:
                return path
            if root.val<target.val:
                dfs(root.right,target,path)
            else:
                dfs(root.left,target,path)
            return path

        p_path = dfs(root,p,[])
        q_path = dfs(root,q,[])
        ans = None
        for k,v in zip(p_path,q_path):
            if k.val == v.val:
                ans = k
        return ans

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if p.val<ancestor.val and q.val<ancestor.val:
                ancestor = ancestor.left
            elif p.val>ancestor.val and q.val>ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor








