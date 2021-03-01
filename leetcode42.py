from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans,high = 0,0
        stack = []
        for i in range(n):
            while stack and height[stack[-1]]<height[i]:
                cur = stack.pop()
                if not stack:break
                l = stack[-1]
                r = i
                high = min(height[l],height[r]) - height[cur]
                ans += (r-l-1)*high
            stack.append(i)
        return ans

solution = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
result = solution.trap(height)
print(result)