#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：17.16.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/29 23:08 
'''
# 同198
from typing import List
class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:return  0
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-2] + nums[i],dp[i-1])
        return dp[-1]