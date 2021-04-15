# 236. 二叉树的最近公共祖先
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # cur = root
        # def search(root:'TreeNode',val:int,count:int):
        #     if not root : return None
        #     if root.val == val: return count
        #     res = search(root.left,val,count+1)
        #     if res!= None:
        #         return res
        #     res = search(root.right,val,count+1)
        #     if res!= None:
        #         return res
        # first_level = search(root,p.val,0)
        # second_level = search(root,q.val,0)

        if not root or root == p or root==q : return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        if not right: return left
        return root




