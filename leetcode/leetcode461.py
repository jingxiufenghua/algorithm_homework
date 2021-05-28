#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode461.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/27 20:54 
'''
from typing import List
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        for i in range(32):
            x_last = x&1
            x = x>>1
            y_last = y&1
            y = y>>1
            if x_last == y_last:
                count += 1
        return count
