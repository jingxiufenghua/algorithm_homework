#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：53_II.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/28 23:50 
'''
# 剑指 Offer 53 - II. 0～n-1中缺失的数字  二分查找
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = 0,n-1
        if nums[0] != 0:return 0
        if nums[-1] != n: return n
        while left <= right:
            mid = (left+right)>>1
            mid_nums = (nums[left]+nums[right])>>1
            if nums[mid] == mid_nums:
                left = mid + 1
            elif nums[mid]>mid:
                right = mid
            else:







