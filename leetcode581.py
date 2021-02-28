from  typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l,r = len(nums),0
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >nums[i]:
                l = min(l,stack.pop())
            stack.append(i)
        stack.clear()
        for j in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<nums[j]:
                r = max(r,stack.pop())
            stack.append(j)
        return r-l+1 if r-l>0 else 0

solution = Solution()
# nums = [2,6,4,8,10,9,15]
nums = [2,1]
# nums = [1,3,2,2,2]
# nums = [2,3,3,2,4]
result = solution.findUnsortedSubarray(nums)
print(result)
