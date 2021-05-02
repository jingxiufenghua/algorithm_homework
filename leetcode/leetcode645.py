#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode645.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/1 0:29 
'''
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        dp = [0]*(n+1)
        dp[0] = 0
        for i in range(n):
            dp[i+1] = dp[i] ^ nums[i]
            if  i>=1 and dp[i+1] == dp[i-1]:
                break
        double = nums[i]
        for j in range(n):
            if j+1 not in nums:
                break
        return [double,j+1]


solution = Solution()
nums =  [3,2,2]
result = solution.findErrorNums(nums)
print(result)
