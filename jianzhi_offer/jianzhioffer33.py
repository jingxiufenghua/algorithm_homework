from typing import List
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i,j):
            if i>=j: return True
            p=i
            while postorder[p] < postorder[j]:p+=1
            m = p
            while postorder[p] > postorder[j]:p+=1
            return p==j and recur(i,m-1) and recur(m,j-1)
        return recur(0,len(postorder)-1)


preorder = [5,2,1,3,6]
inorder = [1,2,3,5,6]
solution = Solution()
verylist = [1,6,3,2,5]
result = solution.verifyPostorder(verylist)
print(result)