from typing import List
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if not nums :return -1
#         n = len(nums)
#         zero = 0
#         for i in range(n):
#             if nums[i] != 0:
#                 nums[i],nums[zero] = nums[zero],nums[i]
#                 zero += 1
#         return nums

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right = 0,0
        for i in range(len(nums)):
            if nums[right]!=0:
                nums[right],nums[left] = nums[left],nums[right]
                left += 1
            right += 1

solution = Solution()
nums = [0,0,1]
result = solution.moveZeroes(nums)
print(nums)
