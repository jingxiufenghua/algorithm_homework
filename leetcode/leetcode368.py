#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode368.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/23 11:44 
'''
# 368. 最大整除子集
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        nums.sort()
        n = len(nums)
        maxNum = 0
        dp = []
        for i in range(n):
            dp.append([])
            dp[i].append(nums[i])
            index = -1
            subMax = -1
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0:
                    if subMax<len(dp[j]):
                        subMax = len(dp[j])
                        index = j
            if index!= -1:
                for k in dp[index]:
                    dp[i].append(k)
            maxNum = max(maxNum,len(dp[i]))
        for  i in range(n):
            if len(dp[i]) == maxNum:
                return dp[i]
        return []








solution = Solution()
matrix = [1,2,4,8]
result = solution.largestDivisibleSubset(matrix)
print(result)

