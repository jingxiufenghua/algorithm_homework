#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode377.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/24 21:15 
'''
# 377. 组合总和 Ⅳ
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.hash_map = {}
        def backtrack(nums:List[int],remains):
            if remains==0:return 1
            if remains in self.hash_map:
                return self.hash_map.get(remains)
            res = 0
            for i in range(len(nums)):
                if remains>=nums[i]:
                    res += backtrack(nums,remains-nums[i])
            self.hash_map[remains] = res
            return res
        return backtrack(nums,target)



