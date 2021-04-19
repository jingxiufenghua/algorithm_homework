#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode480.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/18 22:58 
'''
from typing import List
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        from sortedcontainers import SortedList
        s = SortedList()
        n = len(nums)
        left = right = 0
        res = []
        while right<n:
            s.add(nums[right])
            while len(s)>k:
                s.remove(nums[left])
                left += 1
            if len(s) == k:
                if k&1 == 1:
                    res.append(s[k/2])
                else:
                    res.append((s[k//2-1]+s[k//2])/2)
            right += 1
        return res
solution = Solution()
nums = [1,4,2,3]
result = solution.medianSlidingWindow(nums,4)
print(result)