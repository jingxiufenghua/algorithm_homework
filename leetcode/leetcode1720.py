#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1720.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/6 9:26 
'''
from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in range(len(encoded)):
            res.append(res[-1]^encoded[i])
        return res

