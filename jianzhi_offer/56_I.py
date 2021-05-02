#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：56_I.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/29 23:37 
'''
# 同主站260
from typing import List
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mask = 0
        for i in range(n):
            mask ^= nums[i]
        div = 1
        while div&mask==0:
            div <<=1
        a,b = 0,0
        for i in nums:
            if i & div == 0:
                a ^= i
            else:
                b ^= i
        return [a,b]



