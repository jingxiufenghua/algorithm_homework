# Definition for a binary tree node.
from typing import List
from leetcode_uitil import buildTree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []
        res = []
        def pre(root):
            if not root:return []
            if not root.left and not root.right:
                res.append(root.val)
                return
            pre(root.left)
            res.append(root.val)
            pre(root.right)
        pre(root)
        return res

preorder = [1,2,3]
inorder = [1,3,2]
input = buildTree(preorder,inorder)
solution = Solution()
result = solution.inorderTraversal(input)
print(result)

