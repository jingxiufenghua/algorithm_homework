#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode315.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/2 23:27 
'''
from typing import List
class Solution:
    # 超出时间限制
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        n = len(nums)
        dp = [0]*n
        dp[n-1] = 0
        for i in range(n-1,-1,-1):
            max_min_number,index,count = 0,n-1,0
            for j in range(n-1,i,-1):
                if nums[j]<nums[i] and max_min_number<nums[j]:
                    max_min_number = nums[j]
                    index = j
            for k in range(index,i,-1):
                if nums[k]<nums[i]:
                    count += 1
            dp[i] = dp[index] + count
        return dp

solution = Solution()
nums = [5,2,6,1]
result = solution.countSmaller(nums)
print(result)


