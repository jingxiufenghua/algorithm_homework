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
# 动态规划
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        max_left,max_right = {},{}
        max_left[0] = height[0]
        max_right[n-1] = height[n-1]
        for i in range(1,n):
            max_left[i] = max(max_left[i-1],height[i])
        for i in range(n-2,-1,-1):
            max_right[i] = max(max_right[i+1],height[i])
        for i in range(n):
            ans+= min(max_left[i],max_right[i])-height[i]
        return ans
# 双指针法
    def trap3(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left,right = 0,n-1
        left_max,right_max = 0,0
        while left<=right:
            if left_max<right_max:
                ans+=max(0,left_max-height[left])
                left_max = max(left_max,height[left])
                left +=1
            else:
                ans+= max(0,right_max-height[right])
                right_max = max(right_max,height[right])
                right-=1
        return ans


solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
# result = solution.trap(height)
result = solution.trap2(height)
print(result)

# 单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        stack = []
        ans,high = 0,0
        for i in range(n):
            while stack and height[stack[-1]]<height[i]:
                cur = stack.pop()
                if not stack: break
                l = stack[-1]
                r = i
                high = min(height[l],height[r]) - height[cur]
                ans += (r-l-1)*high
            stack.append(i)
        return ans





class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        left,right = 0,n-1
        left_max,right_max = 0,0
        ans = 0
        while left<=right:
            if left_max<right_max:
                ans += max(0,left_max-height[left])
                left_max = max(left_max,height[left])
                left += 1
            else:
                ans += max(0,right_max-height[right])
                right_max = max(right_max,height[right])
                right -= 1
        return ans



class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        stack = []
        ans = 0
        for i in range(n):
            while stack and height[stack[-1]]<height[i]:
                cur = stack.pop()
                if not stack : break
                l = stack[-1]
                r = i
                high = min(height[l],height[r]) - height[cur]
                ans += (r-l-1)*high
            stack.append(i)
        return ans


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0
        n = len(height)
        left_max,right_max = {},{}
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]
        ans = 0
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i])
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])
        for i in range(n):
            ans += min(left_max[i],right_max[i]) - height[i]
        return ans



class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : return 0
        n = len(height)
        ans,high = 0,0
        stack = []
        for i in range(n):
            while stack and height[stack[-1]]<height[i]:
                cur = stack.pop()
                if not stack: break
                l = stack[-1]
                r = i
                high = min(height[l],height[r]) - height[cur]
                ans += (r-l-1)*high
            stack.append(i)
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        max_left,max_right = {},{}
        max_left[0] = height[0]
        max_right[n-1] = height[n-1]
        ans = 0
        for i in range(1,n):
            max_left[i] = max(max_left[i-1],height[i])
        for i in range(n-2,-1,-1):
            max_right[i] = max(max_right[i+1],height[i])
        for i in range(n):
            ans += min(max_left[i],max_right[i]) - height[i]
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        ans = 0
        left,right = 0,n-1
        left_max,right_max = 0,0
        while left<=right:
            if left_max<right_max:
                ans += max(0,left_max-height[left])
                left_max = max(left_max,height[left])
                left += 1
            else:
                ans += max(0,right_max-height[right])
                right_max = max(right_max,height[right])
                right -= 1
        return ans


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        left_max,right_max = {},{}
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]
        ans = 0
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i])
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])
        for i in range(n):
            ans += min(left_max[i],right_max[i]) - height[i]
        return ans





























