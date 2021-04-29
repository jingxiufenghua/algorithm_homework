#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：56_I.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/29 23:37 
'''
from typing import List
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
