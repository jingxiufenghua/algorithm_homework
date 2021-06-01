#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework
@File    ：leetcode394.py
@IDE     ：PyCharm
@Author  ：无名
@Date    ：2021/5/31 16:32
'''
from typing import List
class Solution:
    def decodeString(self, s: str) -> str:
        if not s : return s
        stack,res,multi = [],"",0
        for c in s:
            if c == "[":
                stack.append([multi,res])
                res,multi = "",0
            elif c == "]":
                cur_multi,last_res = stack.pop()
                res = last_res + cur_multi*res
            elif "0"<=c<="9":
                multi = multi*10 + int(c)
            else:
                res += c
        return  res


solution = Solution()
s = "3[a]2[bc]"
result = solution.decodeString(s)
print(result)


class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)

solution = Solution()
s = "3[a]2[bc]"
result = solution.decodeString(s)
print(result)


class Solution:
    def decodeString(self, s: str) -> str:
        if not s : return s
        stack,multi,res = [],0,""
        for c in s:
            if c == "[":
                stack.append([multi,res])
                multi = 0
                res = ""
            elif c == "]":
                cur_multi,last_res = stack.pop()
                res = last_res + cur_multi*res
            elif "0"<=c<="9":
                multi = multi*10 + int(c)
            else:
                res += c
        return res

class Solution:
    def decodeString(self, s: str) -> str:
        if not s: return s
        stack,multi,res = [],0,""
        for c in s:
            if c == "[":
                stack.append([multi,res])
                multi,res = 0,""
            elif c == "]":
                cur_multi,last_res = stack.pop()
                res = last_res + res*cur_multi
            elif "0"<=c<="9":
                multi = multi*10 + int(c)
            else:
                res += c
        return res