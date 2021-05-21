#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1035.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/21 9:50 
'''
from typing import List
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2 = len(nums1),len(nums2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i,num1 in enumerate(nums1):
            for j,num2 in enumerate(nums2):
                if num1 == num2:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]



