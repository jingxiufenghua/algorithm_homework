#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode75.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/24 16:32 
'''
# from typing import List
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         def quick_sort(list,i,j):
#             if i>=j:
#                 return list
#             pivot = list[i]
#             low = i
#             high = j
#             while i<j:
#                 while i<j and list[j]>=pivot:
#                     j -= 1
#                 list[i] = list[j]
#                 while i<j and list[i]<=pivot:
#                     i += 1
#                 list[j] = list[i]
#             list[j] = pivot
#             quick_sort(list,low,i-1)
#             quick_sort(list,i+1,high)
#             return list
#         quick_sort(nums,0,len(nums)-1)
#
# solution = Solution()
# nums = [2,0,2,1,1,0]
# result = solution.sortColors(nums)
# print(result)

#
# def partition(arr, low, high):
#     i = (low - 1)  # 最小元素索引
#     pivot = arr[high]
#
#     for j in range(low, high):
#
#         # 当前元素小于或等于 pivot
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
#
#
# # arr[] --> 排序数组
# # low  --> 起始索引
# # high  --> 结束索引
#
# # 快速排序函数
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
#
# arr = [3,6,7,5,9,10,5,11,7]
# n = len(arr)
# quickSort(arr,0,n-1)
# print ("排序后的数组:")
# for i in range(n):
#     print ("%d" %arr[i])



class Solution:
    def Sort(self,nums):
        n = len(nums)
        def quickSort(nums,low,high):
            if low<high:
                pi = partition(nums,low,high)
                quickSort(nums,low,pi-1)
                quickSort(nums,pi+1,high)

        def partition(nums,low,high):
            pivot = nums[low]
            while low<high:
                while low<high and nums[high]>pivot:
                    high -= 1
                nums[low] = nums[high]
                while low<high and nums[low]<=pivot:
                    low += 1
                nums[high] = nums[low]
            nums[low] = pivot
            return low
        quickSort(nums,0,n-1)

solution = Solution()
arr = [3,6,7,5,9,10,5,11,7]
result = solution.Sort(arr)
print(arr)


