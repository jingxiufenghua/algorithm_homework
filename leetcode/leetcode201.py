#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode201.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/30 10:17 
'''
from typing import List
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        mask = 1<<30
        ans = 0
        while mask>0 and (left&mask)==(right&mask):
            ans |= left&mask
            mask>>=1
        return ans

    # 超时
    # def rangeBitwiseAnd(self, left: int, right: int) -> int:
    #     res = left
    #     tmp = left+1
    #     while tmp<=right:
    #         res &= tmp
    #         tmp +=1
    #     return res

