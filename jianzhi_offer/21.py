# 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
from typing import List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        left,right = 0,len(nums)
        while left<right:
            if nums[right]&1 == 0 :
                right -= 1
                continue
            if nums[left]&1 == 1:
                left +=1
                continue
            nums[left],nums[right] = nums[right],nums[left]
        return nums

    # def exchange(self, nums: List[int]) -> List[int]:
    #     if not nums : return nums
    #     i,n = 0,len(nums)
    #     ods = []
    #     while i<len(nums):
    #         if nums[i]&1==1:
    #             ods.append(nums[i])
    #             del(nums[i])
    #         else:
    #             i += 1
    #     return ods + nums

solution = Solution()
n = [1,2,3,4]
result = solution.exchange(n)
print(result)
