# Definition for a binary tree node.
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def _maxPathSum(self,root: TreeNode):
        if not root: return  -sys.maxint
        l = max(0,self._maxPathSum(root.left))
        r = max(0,self._maxPathSum(root.right))
        self.ans = max(self.ans,root.val+l+r)
        return root.val + max(l,r)

    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -sys.maxint
        self._maxPathSum(root)
        return self.ans

