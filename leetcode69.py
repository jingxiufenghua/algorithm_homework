import  numpy as np
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x==0 or x==1:return x
#         stack = []
#         for i in range(x+1):
#             while i**2>x:
#                 res = stack[-1]
#                 return res
#             stack.append(i)

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0:
#             return 0
#         ans = int(math.exp(0.5 * math.log(x)))
#         return ans + 1 if (ans + 1) ** 2 <= x else ans

class Solution:
    def mySqrt(self, x: int) -> int:
        l,r,ans = 0,x,-1
        while l<r:
            mid = (l+r)//2
            if mid**2<=x:
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans



solution = Solution()
n = 2
result = solution.mySqrt(n)
print(result)