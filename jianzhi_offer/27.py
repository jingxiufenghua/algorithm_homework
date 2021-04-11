# 剑指 Offer 27. 二叉树的镜像
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # def changeTraversal(head):
        #     if head:
        #         temp = head.left
        #         head.left = head.right
        #         head.right = temp
        #         changeTraversal(head.left)
        #         changeTraversal(head.right)
        #
        # if root:
        #     changeTraversal(root)
        #     return root
        if root:
            root.left,root.right = root.right,root.left
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
            return root



class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
            return root

