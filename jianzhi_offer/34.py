# Definition for a binary tree node.
from  typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root: return []
        # 以下方法错误
        # res = []
        # def search(root,sum,list,target):
        #     if not root: return
        #     list = list[:]
        #     if sum + root.val <= target:
        #         sum = sum + root.val
        #         list.append(root.val)
        #         if sum ==  target:
        #             res.append(list)
        #             return
        #         else:
        #             search(root.left,sum,list,target)
        #             search(root.right,sum,list,target)
        # search(root,0,[],target)
        # return res

        res,path = [],[]
        def recur(root,tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(path)
            recur(root.left,tar)
            recur(root.right,tar)
            path.pop()
        recur(root,target)
        return res



from leetcode_uitil import buildTree
# preorder = [5,4,11,7,2,8,13,4,1]
# inorder = [7,11,2,4,5,13,8,4,1]
# result = buildTree(preorder,inorder)

# preorder = [5,4,11,7,2,8,13,3,6,1]
# inorder = [7,11,2,4,5,13,8,6,3,1]
# result = buildTree(preorder,inorder)
solution = Solution()
result = TreeNode(1)
result = solution.pathSum(result,0)
print(result)
