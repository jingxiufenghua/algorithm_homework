#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：45.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/28 18:33 
'''
# 剑指 Offer 45. 把数组排成最小的数  对比 179 最大的数
from typing import List
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        key = cmp_to_key(lambda x,y : int(x+y) - int(y+x))
        res = "".join(sorted(map(str,nums),key=key,reverse=True)).lstrip("0")
        return res or "0"
