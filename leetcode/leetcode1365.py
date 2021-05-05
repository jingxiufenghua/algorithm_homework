#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1365.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/3 23:52 
'''
from typing import List
import collections
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nn = sorted(nums)
        dict = {}
        for i,n in enumerate(nn):
            if n not in dict:
                dict[n] = i
        nn = []
        for n in nums:
            nn.append(dict[n])
        return nn



solution = Solution()
nums = [8,1,2,2,3]
result = solution.smallerNumbersThanCurrent(nums)
print(result)


