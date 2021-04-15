"""
# Definition for a Node.
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点
                self.head = cur
            self.pre = cur  # 保存 cur
            dfs(cur.righ)  # 递归右子树
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left)
            if self.pre:
                self.pre.right,cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left,self.pre.right = self.pre,self.head
        return self.head