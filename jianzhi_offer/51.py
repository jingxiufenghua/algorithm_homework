#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：51.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/4 16:47 
'''
# 剑指 Offer 51. 数组中的逆序对
from typing import List
# class Solution:
    # 超时
    # def reversePairs(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     count = 0
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             if nums[j]<nums[i]:
    #                 count += 1
    #     return count

    #  这个官方JAVA改写的python版本也超时 ^_^
    # def reversePairs(self, nums: List[int]) -> int:
    #     def reversePairs(nums,left,right,temp):
    #         if left == right:
    #             return 0
    #         mid = left + ((right-left)>>1)
    #         leftpairs = reversePairs(nums,left,mid,temp)
    #         rightpairs= reversePairs(nums,mid+1,right,temp)
    #         if nums[mid]<=nums[mid+1]:
    #             return leftpairs + rightpairs
    #         crosspairs = mergeAndcount(nums,left,mid,right,temp)
    #         return leftpairs + rightpairs + crosspairs
    #     def  mergeAndcount(nums,left,mid,right,temp):
    #         temp = nums[:]
    #         i,j = left,mid+1
    #         count = 0
    #         for k in range(left,right+1):
    #             if i == mid+1:
    #                 nums[k] = temp[j]
    #                 j += 1
    #             elif j == right+1:
    #                 nums[k] = temp[i]
    #                 i +=1
    #             elif temp[i]<=temp[j]:
    #                 nums[k] = temp[i]
    #                 i += 1
    #             else:
    #                 nums[k] = temp[j]
    #                 j += 1
    #                 count += (mid-i+1)
    #         return count
    #
    #     n = len(nums)
    #     if n<2 : return  0
    #     copy = nums[:]
    #     temp = [0]*n
    #     return reversePairs(copy,0,n-1,temp)
    #
    # class Solution:
    #     def mergeSort(self, nums, tmp, l, r):
    #         if l >= r:
    #             return 0
    #
    #         mid = (l + r) // 2
    #         inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
    #         i, j, pos = l, mid + 1, l
    #         while i <= mid and j <= r:
    #             if nums[i] <= nums[j]:
    #                 tmp[pos] = nums[i]
    #                 i += 1
    #                 inv_count += (j - (mid + 1))
    #             else:
    #                 tmp[pos] = nums[j]
    #                 j += 1
    #             pos += 1
    #         for k in range(i, mid + 1):
    #             tmp[pos] = nums[k]
    #             inv_count += (j - (mid + 1))
    #             pos += 1
    #         for k in range(j, r + 1):
    #             tmp[pos] = nums[k]
    #             pos += 1
    #         nums[l:r + 1] = tmp[l:r + 1]
    #         return inv_count
    #
    #     def reversePairs(self, nums: List[int]) -> int:
    #         n = len(nums)
    #         tmp = [0] * n
    #         return self.mergeSort(nums, tmp, 0, n - 1)


#       self 函数运行的快一点
class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0
        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return inv_count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)

solution = Solution()
nums =  [7,5,8,9]
result = solution.reversePairs(nums)
print(result)
