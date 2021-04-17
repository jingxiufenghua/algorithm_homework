# 783. 二叉搜索树节点最小距离
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
first = TreeNode(44)
second = TreeNode(50,first)
thrid = TreeNode(58,second)
four = TreeNode(34,None,thrid)
root = TreeNode(27,None,four)
# import heapq
import numpy as np
# class Solution:
#     def minDiffInBST(self, root: TreeNode) -> int:
#         heap = []
#         heapq.heapify(heap)
#         def recur(root):
#             if not root: return
#             heapq.heappush(heap,root.val)
#             recur(root.left)
#             recur(root.right)
#         recur(root)
#         min_diff = np.inf
#         first = heapq.heappop(heap)
#         while heap:
#             second = heapq.heappop(heap)
#             diff = second - first
#             min_diff = min(min_diff,diff)
#             first = second
#         return min_diff

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def inorder(root):
            if not root: return
            inorder(root.left)
            if self.pre:
                self.ans = min(self.ans,root.val - self.pre)
            self.pre = root.val
            inorder(root.right)
        self.ans,self.pre = np.inf,None
        inorder(root)
        return self.ans
# class Solution(object):
#     def minDiffInBST(self, root):
#         self.prev = None
#         self.minDiff = 10e6
#         self.inOrder(root)
#         return self.minDiff
#
#     def inOrder(self, root):
#         if not root:
#             return
#         self.inOrder(root.left)
#         if self.prev:
#             self.minDiff = min(root.val - self.prev.val, self.minDiff)
#         self.prev = root
#         self.inOrder(root.right)

solution = Solution()
result = solution.minDiffInBST(root)
print(result)












import numpy as np
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def recur(root):
            if not root: return
            recur(root.left)
            if self.pre:
                self.ans = min(self.ans,root.val - self.pre)
            self.pre = root.val
            recur(root.right)
        self.ans,self.pre = np.inf,None
        return self.ans




class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.prev = None
        self.mindiff = 10e6
        self.inorder(root)
        return self.mindiff
    def inorder(self,root):
        if not root: return
        self.inorder(root.left)
        if self.prev:
            self.mindiff = min(self.mindiff,root.val-self.prev.val)
        self.prev = root
        self.inorder(root.right)






























