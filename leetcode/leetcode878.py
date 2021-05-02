#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode878.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/2 22:59 
'''
# 878. 第 N 个神奇数字  类似 1201
from typing import List
from math import gcd
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def magic_count(x):
            return  x//a + x//b - x//(a*b//gcd(a,b))
        l = 1
        r = n*min(a,b)
        while l<r:
            m = (l+r)>>1
            k = magic_count(m)
            if k<n: l = m + 1
            else: r = m
        return int(l%(1e9+7))

