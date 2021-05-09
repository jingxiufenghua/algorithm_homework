#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：2.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/9 10:23 
'''
from typing import List
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2 = len(nums1),len(nums2)
        ans = 0
        for i in range(n1):
            l = i
            r = n2-1
            while l<r:
                mid = (l+r+1)//2
                if nums2[mid]>=nums1[i] :
                    l = mid
                else:
                    r = mid - 1
            ans = max(ans, l - i)
        return ans
solution = Solution()
nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]
result = solution.maxDistance(nums1,nums2)
print(result)


# class Solution(object):
#     def maxDistance(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: int
#         """
#         r = 0
#         n = len(nums1)
#         m = len(nums2)
#         ans = 0
#
#         for l in range(n):
#             while r < m - 1 and nums2[r + 1] >= nums1[l]:
#                 r += 1
#             if nums2[r] >= nums1[l]:
#                 ans = max(ans, r - l)
#         return ans