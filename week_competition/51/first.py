#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：first.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/1 22:14 
'''
from typing import List
class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c,x):
            return chr(ord(c)+int(x))
        word = list(s)
        for i in range(len(s)):
            if i&1 == 0:
                continue
            word[i] = shift(word[i-1],word[i])
        return ''.join(word)
solution = Solution()
s = "a1c1e1"
result = solution.replaceDigits(s)
print(result)
