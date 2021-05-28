#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode152.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/23 11:06 
'''
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max, dp_min = nums[0],nums[0]
        maxp = nums[0]
        for i in range(1,len(nums)):
            # 　注意 这里必须是同时更新
            dp_max, dp_min = max(nums[i], dp_max*nums[i], dp_min*nums[i]), min(nums[i], dp_max*nums[i], dp_min*nums[i])
            maxp = max(maxp, dp_max)
        return maxp


cluster by
cluster by