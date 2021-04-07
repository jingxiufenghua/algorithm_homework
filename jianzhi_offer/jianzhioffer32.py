# 剑指 Offer 32 - II. 从上到下打印二叉树 II
# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 队列 BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res

# DFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.level(root,0,res)
        return res

    def level(self,root,level,res):
        if not root:return
        if level==len(res): res.append([])
        res[level].append(root.val)
        if root.left: self.level(root.left,level+1,res)
        if root.right: self.level(root.right,level+1,res)


