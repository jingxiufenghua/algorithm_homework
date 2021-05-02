# 1. 采购方案
from typing import  List
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        if not nums :return -1
        nums.sort()
        res = 0
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i] + nums[j]>target:
                j-=1
            else:
                res = res + (j-i)
                i = i + 1
        return res%1000000007






solution = Solution()
nums = [2,5,3,5]
result = solution.purchasePlans(nums,6)
print(result)


class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        matrix_x = num - xPos - 1
        matrix_y = num - yPos - 1

        step_over = num**2 - min(matrix_x,matrix_y)



# class Solution:
#     def magicTower(self, nums: List[int]) -> int:
#         n = len(nums)
#         if sum(nums)<= -1 :return -1
#         blood = 1
#         dp = []
#         count = 0
#         while len(nums)>=1:
#             if blood+nums[0]<=0:
#                 nums.append(nums[0])
#                 del nums[0]
#                 count = count + 1
#                 if blood + nums[0]<=0:
#                     return -1
#             blood = blood +nums[0]
#             del nums[0]
#         return count
#
# solution = Solution()
# nums = [100,100,100,-250,-60,-140,-50,-50,100,150]
# result = solution.magicTower(nums)
# print(result)