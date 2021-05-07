#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：01.09.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 0:15 
'''
from typing import List
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1),len(s2)
        if s1 == s1 : return True
        if n1 != n2 :return False
        new = s2*2
        for j in range(n1*2):
            if s1 == new[j:j+n1]:
                return True
        return False
solution = Solution()
result = solution.isFlipedString("","")
print(result)
