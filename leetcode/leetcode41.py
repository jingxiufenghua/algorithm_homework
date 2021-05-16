#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode41.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/15 15:01 
'''
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        new = list(set(nums))
        new.sort()
        n = len(new)
        if new[0]>1: return 1
        for i in range(1,n):
            if new[i]<=0:
                continue
            elif new[i-1]<=0 and new[i] >1:
                return 1
            elif new[i]==new[i-1]+1 or (new[i-1]<=0 and new[i]==1):
                continue
            else:
                return new[i-1] + 1
        return new[-1] + 1 if new[-1]+1>=1 else 1
solution = Solution()
nums = [-5]
result = solution.firstMissingPositive(nums)
print(result)


