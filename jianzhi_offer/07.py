# 剑指 Offer 07. 重建二叉树
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:return  None
        head = TreeNode(preorder[0])
        for i in range(len(preorder)):
            


