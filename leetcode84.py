from  typing import  List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            right,left = i,i
            while left>=0 and heights[left] >= heights[i]:
                left -=1
            while right<n and heights[right] >= heights[i]:
                right+=1
            res = max(res,(right-left-1)*heights[i])
        return res
solution = Solution()
nums = [2,1,5,6,2,3]
# nums = [2,4]
result = solution.largestRectangleArea(heights=nums)
print(result)
