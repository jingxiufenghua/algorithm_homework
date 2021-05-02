#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：1.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/2 10:10 
'''
from typing import List
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        dis = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == target:
                dis = abs(i-start)
                ans = min(ans,dis)
        return ans