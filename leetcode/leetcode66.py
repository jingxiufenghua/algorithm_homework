#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode66.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/3 20:52 
'''
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        flag = 1
        for i in range(n-1,-1,-1):
            if digits[i] + flag <10:
                digits[i] = digits[i] + flag
                flag = 0
            else:
                digits[i] = (digits[i] + 1)%10
                flag = 1
        if flag == 1:
            return [1] + digits
        else:
            return digits
