from  typing import List
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         l,r = len(nums),0
#         stack = []
#         for i in range(len(nums)):
#             while stack and nums[stack[-1]] >nums[i]:
#                 l = min(l,stack.pop())
#             stack.append(i)
#         stack.clear()
#         for j in range(len(nums)-1,-1,-1):
#             while stack and nums[stack[-1]]<nums[j]:
#                 r = max(r,stack.pop())
#             stack.append(j)
#         return r-l+1 if r-l>0 else 0
class Solution:
    def findUnsortedSubarray(self, s: str) -> bool:
        n = len(s)
        r = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if s[j]<s[i]:
                    r = max(r,j)
                    l = min(n,i)
        return r-l+1 if r-1>0 else 0

solution = Solution()
# nums = [2,6,4,8,10,9,15]
nums = [1,6,2,5,9]
# nums = [1,3,2,2,2]
# nums = [2,3,3,2,4]
result = solution.findUnsortedSubarray(nums)
print(result)
