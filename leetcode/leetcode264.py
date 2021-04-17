# 264. 丑数 II
# 超出时间限制
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         def isUglyNumber(n):
#             if n<=0:
#                 return False
#             factors = [2,3,5]
#             for factor in factors:
#                 while n%factor == 0:
#                     n //=factor
#             return n==1
#         count = 0
#         i = 1
#         while count<n:
#             if isUglyNumber(i):
#                 count += 1
#             i += 1
#         return  i-1

import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                nxt = curr*factor
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return heapq.heappop(heap)

solution = Solution()
n = 5
result = solution.nthUglyNumber(n)
print(result)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        p2=p3=p5=1
        for i in range(2,n+1):
            nums2,nums3,nums5 = dp[p2]*2,dp[p3]*3,dp[p5]*5
            dp[i] = min(nums2,nums3,nums5)
            if dp[i] == nums2:
                p2 += 1
            if dp[i] == nums3:
                p3 += 1
            if dp[i] == nums5:
                p5 += 1
        return dp[n]






