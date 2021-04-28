#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode633.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/28 14:13 
'''
from typing import List
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        b = math.ceil(math.sqrt(c))
        a = 0
        while a<=b:
            if a**2 + b**2> c:
                b-=1
            elif a**2 + b**2<c:
                a += 1
            else:
                return True
        return False


