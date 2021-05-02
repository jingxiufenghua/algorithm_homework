#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：39.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/30 17:17 
'''
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[:n//2]


