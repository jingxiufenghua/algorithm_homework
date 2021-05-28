#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode215.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/11 23:02 
'''
from typing import List
# import heapq
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         res = []
#         heapq.heapify(res)
#         for i in range(n):
#             if nums[i] in res:
#                 continue
#             heapq.heappush(res,nums[i])
#             if len(res) > k:
#                 heapq.heappop(res)
#         for i in range(k-1):
#             heapq.heappop(res)
#         return heapq.heappop(res)



#
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def partition(nums,low,high):
#             pivot = nums[low]
#             while low<high:
#                 while low<high and nums[high]>=pivot:
#                     high -= 1
#                 nums[low] = nums[high]
#                 while low<high and nums[low]<pivot:
#                     low += 1
#                 nums[high] = nums[low]
#             nums[low] = pivot
#             return low
#         def quickSort(nums,low,high):
#             if low<high:
#                 pi = partition(nums,low,high)
#                 quickSort(nums,low,pi-1)
#                 quickSort(nums,pi+1,high)
#
#         quickSort(nums,0,len(nums)-1)
#         return nums[-k]
#
# solution = Solution()
# nums = [3,2,1,5,6,4]
# result = solution.findKthLargest(nums,2)
# print(result)

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def partition(nums,low,high):
#             pivot = nums[low]
#             while low<high:
#                 while low<high and nums[high]>=pivot:
#                     high -= 1
#                 nums[low] = nums[high]
#                 while low<high and nums[low]<pivot:
#                     low += 1
#                 nums[high] = nums[low]
#             nums[low] = pivot
#             return low
#         n = len(nums)
#         left,right = 0,n-1
#         target = n-k
#         while True:
#             pi = partition(nums,left,right)
#             if pi == target:
#                 return nums[pi]
#             elif pi<target:
#                 left = pi+1
#             else:
#                 right = pi-1
#
#
# solution = Solution()
# nums = [1]
# result = solution.findKthLargest(nums,1)
# print(result)

class Solution:
    def partition(self,nums,low,high):
        pivot = nums[low]
        while low<high:
            while low<high and nums[high]>=pivot:
                high -= 1
            nums[low] = nums[high]
            while low<high and nums[low]<pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low

    def quickSort(self,nums,low,high):
        if low<high:
            pi = self.partition(nums,low,high)
            self.quickSort(nums,low,pi-1)
            self.quickSort(nums,pi+1,high)
    def sort(self,nums):
        low,high = 0,len(nums)-1
        self.quickSort(nums,low,high)

solution = Solution()
nums = [3,5,4,2,6]
result = solution.sort(nums)
print(nums)





