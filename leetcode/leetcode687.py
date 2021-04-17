# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        def longestUnivalue(root: TreeNode) -> int:
            if not root:return 0
            left_length =  longestUnivalue(root.left)
            right_length =  longestUnivalue(root.right)
            left_arrow = right_arrow= 0
            if root.left and root.left.val == root.val:
                left_arrow = left_length + 1
            if root.right and root.right.val == root.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans,left_arrow+right_arrow)
            return max(left_arrow,right_arrow)
        longestUnivalue(root)
        return self.ans
