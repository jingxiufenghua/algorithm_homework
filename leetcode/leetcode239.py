#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode239.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/6/1 17:51 
'''
from typing import List
import heapq
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         q = [(-nums[i],i) for i in range(k)]
#         heapq.heapify(q)
#         ans = [-q[0][0]]
#         for i in range(k,n):
#             heapq.heappush(q,(-nums[i],i))
#             while  q[0][1] <= i-k:
#                 heapq.heappop(q)
#             ans.append((-q[0][0]))
#         return ans




class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        window,res = [],[]
        for i,x in enumerate(nums):
            if i>=k and window[0] <= i-k:
                window.pop(0)
            while window and nums[window[-1]]<=x:
                window.pop()
            window.append(i)
            if i>=k-1:
                res.append(nums[window[0]])
        return res

solution = Solution()
nums = [-1,3,1,2,5,6]
result = solution.maxSlidingWindow(nums,3)
print(result)

