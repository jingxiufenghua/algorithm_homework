#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode313.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/1 21:42 
'''
from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0]*(n+1)
        m = len(primes)
        p = [1]*m
        nums = [0]*m
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(m):
                nums[j] = dp[p[j]]*primes[j]
            dp[i] = min(nums)
            for k in range(m):
                if dp[i] == nums[k]:
                    p[k] += 1
                    # break  千万不能加
        return dp[n]

solution = Solution()
primes = [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]
result = solution.nthSuperUglyNumber(100000,primes)
print(result)



