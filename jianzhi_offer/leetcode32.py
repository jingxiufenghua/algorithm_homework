# 剑指 Offer 32 - I. 从上到下打印二叉树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        def dfs(root,i):
            if not root: return None
            if i == len(res): res.append([])
            res[i].append(root.val)
            dfs(root.left,i+1)
            dfs(root.right,i+1)
        res = []
        dfs(root,0)
        return [j for nums in res for j in nums]
