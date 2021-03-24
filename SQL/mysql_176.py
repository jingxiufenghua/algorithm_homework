# select Salary as SecondHighestSalary
# from Employee
# order by Salary
# limit 1 offset 1
from typing import List
# class Solution:
#     def max_sub_sum(self,nums:List[int])->int:
#         n = len(nums)
#         if n<2:return nums[0]
#         if max(nums)<0:return max(nums)
#         max_sum,sub_sum = 0,0
#         for i in range(n):
#             sub_sum = max(sub_sum+nums[i],sub_sum)
#             max_sum = max(max_sum,sub_sum)
#         return max_sum

class Solution:
    def quickSort(self,nums:List[int])->List[int]:
        if len(nums)<2:return  nums
        pivot = nums[0]
        left = [nums[i] for i in range(1,len(nums)) if nums[i]<pivot]
        right = [nums[j] for j in range(1,len(nums)) if nums[j]>=pivot]
        return self.quickSort(left) + [pivot] + self.quickSort(right)



