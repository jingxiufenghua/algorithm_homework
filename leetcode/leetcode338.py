#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode338.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/15 12:31 
'''
from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        def countOnes(x:int):
            ones = 0
            while x>0:
                x &= (x-1)
                ones += 1
            return ones
        bits = [countOnes(i) for i in range(num+1)]
        return bits