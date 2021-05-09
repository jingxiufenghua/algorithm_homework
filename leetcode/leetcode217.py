#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode217.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 23:11 
'''
from typing import List
# 217. 存在重复元素
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) == len(nums)