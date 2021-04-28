#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：05.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/28 17:19 
'''
from typing import List
class Solution:
    def replaceSpace(self, s: str) -> str:
        if not s:return ""
        word = s.split(" ")
        print(word)
        res = ""
        for i in word:
            res += i + "%20"
        return res[:-len("%20")]

solution = Solution()
s = "     "
result = solution.replaceSpace(s)
print(result)