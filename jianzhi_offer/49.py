#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：49.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/1 20:21 
'''
from typing import List
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        p2=p3=p5=1
        for i in range(2,n+1):
            nums2,nums3,nums5 = dp[p2]*2,dp[p3]*3,dp[p5]*5
            dp[i] = min(nums2,nums3,nums5)
            if nums2 == dp[i]:
                p2 += 1
            if nums3 == dp[i]:
                p3 += 1
            if nums5 == dp[i]:
                p5 += 1
        return dp[n]