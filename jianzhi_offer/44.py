#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：44.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/2 23:43 
'''
# 剑指 Offer 44. 数字序列中某一位的数字
from typing import List
class Solution:
    def findNthDigit(self, n: int) -> int:
        dight,start,count = 1,1,9
        while n>count:
            n -= count
            start *= 10
            dight += 1
            count = 9*start*dight
        num = start + (n-1)//dight
        return int(str(num)[(n-1)%dight])


