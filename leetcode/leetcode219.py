#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode219.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/3 22:59 
'''
from typing import List
class Solution:
    # 超时
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums: return False
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,i+k+1):
                if j>n-1: break
                if nums[i] == nums[j]:
                    return True
        return False
# 散列表 hash_map
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums: return False
        n = len(nums)
        hash_map = set()
        for i in range(n):
            if nums[i] in hash_map: return True
            hash_map.add(nums[i])
            if len(hash_map)>k:
                hash_map.remove(nums[i-k])
        return False


