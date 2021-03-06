# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        left,right = 0,0
        while root.left:
            left +=1
            left += self.maxDepth(root.left)
        while root.right:
            right+=1
            right+=self.maxDepth(root.right)
        return  max(left,right)

