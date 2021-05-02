# 136. 只出现一次的数字
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in nums:
            res ^= i
        return res

        # res = nums[0]
        # for i in range(1,n):
        #     res = res^nums[i]
        # return res
solution = Solution()
nums = [2,1,2]
result = solution.singleNumber(nums)
print(result)


