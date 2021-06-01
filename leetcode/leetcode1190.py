#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1190.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/31 11:04 
'''
from typing import List
class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s:return s
        stack = []
        string = ""
        for c in s:
            if c == "(":
                stack.append(string)
                string = ""
            elif c == ")":
                string = string[::-1]
                string = stack[-1] + string
                stack.pop()
            else:
                string += c
        return string



solution = Solution()
s = "(ul)ao(t(y)qbn)()sj"
result = solution.reverseParentheses(s)
print(result)
