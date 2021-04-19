#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1438.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/17 15:42 
'''
# 1438. 绝对差不超过限制的最长连续子数组
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from sortedcontainers import SortedList
        s = SortedList()
        left = right = res = 0
        n = len(nums)
        while right<n:
            s.add(nums[right])
            while s[-1] - s[0]>limit:
                s.remove(nums[left])
                left += 1
            res = max(res,right-left+1)
            right += 1
        return res



solution = Solution()
nums = [8,2,4,7]
result = solution.longestSubarray(nums,4)
print(result)

