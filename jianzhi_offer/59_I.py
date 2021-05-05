#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：59_I.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/4 23:09 
'''
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left,right = 0,0
        res = []
        while right<n:
            while len(nums[left:right+1])>k:
                left += 1
            if len(nums[left:right+1]) == k:
                res.append(max(nums[left:right+1]))
            right += 1
        return res

solution = Solution()
nums = [1,-1]
result = solution.maxSlidingWindow(nums,1)
print(result)