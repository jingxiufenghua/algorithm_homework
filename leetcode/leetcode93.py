#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode93.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/15 22:19 
'''
from typing import List
# 93. 复原 IP 地址
from collections import Counter
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        SEG_COUNT = 4
        ans = []
        segments = [0]*SEG_COUNT
        def dfs(segId:int ,segStart:int):
            if segId == SEG_COUNT:
                if segStart == len(s):
                    ipAddr = ".".join(str(seg) for seg in segments)
                    ans.append(ipAddr)
                return
            if segStart == len(s):
                return
            if s[segStart] == "0":
                segments[segId] = 0
                dfs(segId+1,segStart+1)
            addr = 0
            for segEnd in range(segStart,len(s)):
                addr = addr*10 + (ord(s[segEnd])-ord("0"))
                if 0<addr<=0xFF:
                    segments[segId] = addr
                    dfs(segId+1,segEnd+1)
                else:
                    break
        dfs(0,0)
        return  ans


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        segCount = 4
        ans = []
        segment = [0]*segCount
        def dfs(segId,segStart):
            if segId == segCount:
                if segStart == len(s):
                    ipAddr = ".".join(str(seg) for seg in segment )
                    ans.append(ipAddr)
                return
            if segStart == len(s):
                return
            if s[segStart] == "0":
                segment[segId] = 0
                dfs(segId+1,segStart+1)
            addr = 0
            for segEnd in range(segStart,len(s)):
                addr = addr*10 + (ord(s[segEnd])-ord("0"))
                if 0<addr<=0xFF:
                    segment[segId] = addr
                    dfs(segId + 1, segEnd + 1)
                else:
                    break
        dfs(0,0)
        return ans



class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        segCount = 4
        ans = []
        segment = [0]*segCount
        def dfs(segId,segStart):
            if segId == segCount:
                if segStart == len(s):
                    ipAddr = ".".join(str(seg) for seg in segment)
                    ans.append(ipAddr)
                return
            if segStart == len(s):
                return
            if s[segStart]== "0":
                segment[segId] = 0
                dfs(segId+1,segStart+1)
            addr = 0
            for segEnd in range(segStart,len(s)):
                addr = addr*10 + (ord(s[segEnd])-ord("0"))
                if 0<addr<=0xFF:
                    segment[segId] = addr
                    dfs(segId + 1, segEnd + 1)
                else:
                    break
        dfs(0,0)
        return ans





























