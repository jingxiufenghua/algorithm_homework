#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode76.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/25 15:41 
'''
from typing import List
import itertools
import collections
class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     ns,nt = len(s),len(t)
    #     res = ""
    #     left,right = 0,0
    #     ans = s
    #
    #     def t_in_s(s,t):
    #         s_dict = collections.Counter(s)
    #         t_dict = collections.Counter(t)
    #         if len(set(s_dict)) < len(set(t_dict)):return False
    #         for i,j in t_dict.items():
    #             if i not in s_dict or j > s_dict[i]:
    #                 return False
    #         return True
    #     if not t_in_s(s,t) : return ""
    #     while left<=ns:
    #         while right<=ns:
    #             if  t_in_s(s[left:right],t):
    #                 if right-left<len(ans):
    #                     ans = s[left:right]
    #                 break
    #             right += 1
    #         left += 1
    #     return ans


    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (i,float("inf"))
        for j,c in enumerate(s):
            if need[c]>0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while True:
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j-i<res[1] - res[0]:
                    res = (i,j)
                need[s[i]] += 1
                needCnt += 1
                i += 1
        return "" if res[1]>


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)  # 记录t中字符出现次数
        window = collections.defaultdict(int)  # 记录窗口中响应的字符出现的次数
        for c in t:
            need[c] += 1

        left, right = 0, 0  # 初始窗口长度为0
        valid = 0  # 用于记录window中t中字符是否出现完，比如：t='abc'，window='abd',valid就等于2.代表need中应该出现的字符在window中才出现了两个，还没有出现完全

        # 记录最小覆盖子串的起始索引及长度
        start = 0
        length = len(s) + 1

        while right < len(s):
            c = s[right]  # 即将加入window的字符c
            right += 1  # 右移窗口

            # 窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:  # window中字符c出现的次数已经达到need所需要的次数时，valid进行更新
                    valid += 1

            # 判断窗口左侧边界是否要收缩
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left

                # d是将移出窗口的字符
                d = s[left]
                # 左移窗口
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:  # 这句话和下面的window[c]-=1不能反，先判断删去的字符c的数量是不是满足need的数量，如果满足，valid将减去1。
                        valid -= 1
                    window[d] -= 1
        # 返回最小覆盖子串
        if length == len(s) + 1:
            return ''
        else:
            return s[start:start + length]





solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
result = solution.minWindow(s,t)
print(result)


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        windows= collections.defaultdict(int)
        for c in t:
            need[c] += 1
        i = 0
        left,right = 0,0
        vaild = 0
        start = 0
        length = len(s)+1
        while right<len(s):
            c = s[right]
            right += 1
            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    vaild += 1
            while vaild == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if windows[d] == need[d]:
                        vaild -= 1
                    windows[d] -= 1
        if length == len(s)+1:
            return  ""
        else:
            return  s[start:start+length]

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        windows = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        left,right = 0,0
        vaild = 0
        start = 0
        length = len(s)+1
        while right<len(s):
            c = s[right]
            right += 1
            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    vaild += 1
            while vaild == len(need):
                if right - left<length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if windows[d] == need[d]:
                        vaild -= 1
                    windows[d] -= 1
        if length == len(s) + 1:
            return  ""
        else:
            return  s[start:start+ length]





class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        windows = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        vaild = 0
        start = 0
        left,right = 0,0
        length = len(s) + 1
        while right<len(s):
            c = s[right]
            right += 1
            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    vaild += 1
            while vaild == len(need):
                if right - left<length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if windows[d] == need[d]:
                        vaild -= 1
                    windows[d] -= 1
        if length == len(s)+1:
            return ""
        else:
            return s[start:start+length]




