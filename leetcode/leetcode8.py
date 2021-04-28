#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode8.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/28 19:28 
'''
from typing import List
#
# INT_MAX = 2 ** 31 - 1
# INT_MIN = -2 ** 31
#
#
# class Automaton:
#     def __init__(self):
#         self.state = 'start'
#         self.sign = 1
#         self.ans = 0
#         self.table = {
#             'start': ['start', 'signed', 'in_number', 'end'],
#             'signed': ['end', 'end', 'in_number', 'end'],
#             'in_number': ['end', 'end', 'in_number', 'end'],
#             'end': ['end', 'end', 'end', 'end'],
#         }
#
#     def get_col(self, c):
#         if c.isspace():
#             return 0
#         if c == '+' or c == '-':
#             return 1
#         if c.isdigit():
#             return 2
#         return 3
#
#     def get(self, c):
#         self.state = self.table[self.state][self.get_col(c)]
#         if self.state == 'in_number':
#             self.ans = self.ans * 10 + int(c)
#             self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
#         elif self.state == 'signed':
#             self.sign = 1 if c == '+' else -1
#
#
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         automaton = Automaton()
#         for c in str:
#             automaton.get(c)
#         return automaton.sign * automaton.ans

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s :return 0
        res,i,sign = 0,1,1
        int_min = -2**31
        int_max= 2**31-1
        bndry = 2**31//10
        if str[0] == "-": sign = -1
        elif str[0] != "+": i = 0
        for c in str[i:]:
            if not "0"<=c<="9":break
            if res> bndry or res == bndry and c > "7" :return int_max if sign == 1 else int_min
            res = 10*res + ord(c)-ord("0")
        return sign*res



