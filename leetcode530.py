# 530. 二叉搜索树的最小绝对差
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,lchild = None,rchild = None):
        self.val = x
        self.left = lchild
        self.right = rchild

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.mindiff = 10e6
        self.prev = None
        self.inorder(root)
        return self.mindiff
    def inorder(self,root):
        if not root: return
        self.inorder(root.left)
        if self.prev:
            self.mindiff = min(self.mindiff,root.val - self.prev.val)
        self.prev = root
        self.inorder(root.right)



first = TreeNode(519)
second = TreeNode(1277,first)
third = TreeNode(2776)
four = TreeNode(2236,second,third)
five = TreeNode(0,None,four)

solution = Solution()
result = solution.getMinimumDifference(five)
print(result)
