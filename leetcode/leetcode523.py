#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode523.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/6/2 15:09 
'''
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n<2 : return False
        left,right = 0,2
        ans = sum(nums[0:right])
        while right<n:
            if ans % k == 0 and ans // k >=1 :
                return True
            ans += nums[right]
            right += 1
