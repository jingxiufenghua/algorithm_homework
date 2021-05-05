#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode740.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/5 9:47 
'''
# 740. 删除并获得点数
from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxvalue = max(nums)
        total = [0]*(maxvalue+1)
        for val in nums:
            total[val] += val
        dp = [0]*(len(total)+1)
        dp[1] = total[0]
        dp[2] = max(total[0],total[1])
        for i in range(2,len(total)+1):
            dp[i] = max(dp[i-2]+total[i-1],dp[i-1])
        return dp[-1]

