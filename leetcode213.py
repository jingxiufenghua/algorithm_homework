# 213. 打家劫舍 II
from typing import List
class Solution:
    def rob(self, nums: List[int]):
        def robrange(nums):
            if not nums: return 0
            n = len(nums)
            if n==1 : return nums[0]
            dp = [0]*n
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,n):
                dp[i] = max(dp[i-1],dp[i-2] + nums[i])
            return dp[-1]
        if not nums: return 0
        n = len(nums)
        if n==1 : return nums[0]
        print(robrange(nums[0:n-1]))
        print(robrange(nums[1:n]))
        return  max(robrange(nums[0:n-1]),robrange(nums[1:n]))



solution = Solution()
nums = [1,3,1,3,100]
result = solution.rob(nums)
print(result)
