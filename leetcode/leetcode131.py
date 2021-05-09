#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode131.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 23:32 
'''
# 131. 分割回文串
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n <= 1 : return []
        for i in range(n):
            s[i]