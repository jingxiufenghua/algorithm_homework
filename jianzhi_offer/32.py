# 剑指 Offer 32 - III. 从上到下打印二叉树
# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        def dfs(root,i):
            if not root: return None
            if i == len(res): res.append([])
            res[i].append(root.val)
            dfs(root.left,i+1)
            dfs(root.right,i+1)
        res = []
        dfs(root,0)
        ans = []
        for i in range(len(res)):
            if i&1==1:
                ans.append(res[i][::-1])
            else:
                ans.append(res[i])
        return ans