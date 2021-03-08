# Definition for a binary tree node.
from typing import List
from leetcode_uitil import buildTree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        left,right = 0,0
        left += self.maxDepth(root.left) + 1
        right+= self.maxDepth(root.right) + 1
        return  max(left,right)


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
input = buildTree(preorder,inorder)
solution = Solution()
result = solution.maxDepth(input)
print(result)
