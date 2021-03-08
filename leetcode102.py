# Definition for a binary tree node.
import collections
from typing import List
from leetcode_uitil import buildTree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
BFS
BFS使用队列，把每个还没有搜索到的点依次放入队列，然后再弹出队列的头部元素当做当前遍历点。BFS总共有两个模板：
如果不需要确定当前遍历到了哪一层，BFS模板如下。
while queue 不空：
    cur = queue.pop()
    for 节点 in cur的所有相邻节点：
        if 该节点有效且未访问过：
            queue.push(该节点)
            
如果要确定当前遍历到了哪一层，BFS模板如下。
这里增加了level表示当前遍历到二叉树中的哪一层了，也可以理解为在一个图中，现在已经走了多少步了。size表示在当前遍历层有多少个元素，也就是队列中的元素数，我们把这些元素一次性遍历完，即把当前层的所有元素都向外走了一步。

level = 0
while queue 不空：
    size = queue.size()
    while (size --) {
        cur = queue.pop()
        for 节点 in cur的所有相邻节点：
            if 该节点有效且未被访问过：
                queue.push(该节点)
    }
    level ++;
"""
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         queue = collections.deque()
#         queue.append(root)
#         res = []
#         while queue:
#             size = len(queue)
#             level = []
#             for _ in range(size):
#                 cur = queue.popleft()
#                 if not cur:
#                     continue
#                 level.append(cur.val)
#                 queue.append(cur.left)
#                 queue.append(cur.right)
#             if level:
#                 res.append(level)
#         return res
"""
DFS
本题使用 DFS 同样能做。由于题目要求每一层的节点都是从左到右遍历，因此递归时也要先递归左子树、再递归右子树。

DFS 做本题的主要问题是： DFS 不是按照层次遍历的。为了让递归的过程中同一层的节点放到同一个列表中，在递归时要记录每个节点的深度 level。递归到新节点要把该节点放入 level 对应列表的末尾。

当遍历到一个新的深度 level，而最终结果 res 中还没有创建 level 对应的列表时，应该在 res 中新建一个列表用来保存该 level 的所有节点。

各语言的代码如下：
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.level(root, 0, res)
        return res

    def level(self, root, level, res):
        if not root: return
        if len(res) == level: res.append([])
        res[level].append(root.val)
        if root.left: self.level(root.left, level + 1, res)
        if root.right: self.level(root.right, level + 1, res)

solution = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
input = buildTree(preorder,inorder)
result = solution.levelOrder(input)
print(result)





