#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode342.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/31 0:06 
'''
from typing import List
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0: return False
        while n%4 == 0:
            n /= 4
        return n==1 or n==-1



class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1

