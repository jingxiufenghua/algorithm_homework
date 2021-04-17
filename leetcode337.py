# 337. 打家劫舍 III
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import numpy as np
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if node == None:
                return 0,0
            left,prel = helper(node.left)
            right,prer = helper(node.right)
            return max(prel+prer+node.val,left+right),left+right
        return helper(root)[0]
