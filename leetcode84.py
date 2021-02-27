# 超出时间限制
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

    def largestRectangleArea1(self, heights: List[int]) -> int:
        n = len(heights)
        left,right = [0]*n,{0}*n

        mono_list = list()
        for i in range(n):
            while mono_list and heights[mono_list[-1]]>=heights[i]:
                mono_list.pop()
            left[i] = mono_list[-1] if mono_list else -1
            mono_list.append(i)

        mono_list = list()
        for i in range(n-1,-1,-1):
            while mono_list and heights[mono_list[-1]] >= heights[i]:
                mono_list.pop()
            right[i] = mono_list[-1] if mono_list else n
            mono_list.append(i)
        ans = max((right[i]-left[i]-1)*heights[i] for i in range(n))  if n>0 else 0
        return ans






solution = Solution()
nums = [2,1,5,6,2,3]
# nums = [2,4]
result = solution.largestRectangleArea(heights=nums)
result1 = solution.largestRectangleArea1(heights=nums)
print(result)
print(result1)
