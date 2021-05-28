#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcoe1353.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/27 12:49 
'''
from typing import List
import heapq
import collections
class Solution:
    def maxEvents(self,events):
        ans, T = 0, 0  # 记录参加的会议数目，最大天数
        # dic_evt[i]是列表,包含在第i天开始的会所有议的结束时间; T是总时间长度
        dic_evt = collections.defaultdict(list)
        for evt in events:
            dic_evt[evt[0]].append(evt[1])
            T = max(T, evt[1])
        # 对时间1～T遍历 每个时刻t,que_able保存当前可参加的会议的结束时间
        que_able = []
        for t in range(1, T + 1):
            for end in dic_evt[t]: heapq.heappush(que_able, end)
            # pop结束时间小于t的会议 参加结束时间大于t的会议中结束时间最早的
            while que_able and que_able[0] < t: heapq.heappop(que_able)
            # 此时que_able中都是结束时间大于t的会议所对应的结束时间
            if que_able:
                ans += 1
                heapq.heappop(que_able)
        return ans

solution = Solution()
events = [[1,1],[1,2],[1,2],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
result = solution.maxEvents(events)
print(result)


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        ans,T = 0,0
        dic_evt = collections.defaultdict(list)
        for evt in events:
            dic_evt[evt[0]].append(evt[1])
            T = max(T,evt[1])
        que_able = []
        for t in range(1,T+1):
            for end in dic_evt[t]: heapq.heappush(que_able,end)
            while que_able and que_able[0]<t: heapq.heappop(que_able)
            if que_able:
                ans += 1
                heapq.heappop(que_able)
        return ans






class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        ans,T = 0,0
        evt_dic = collections.defaultdict(list)
        for evt in events:
            evt_dic[evt[0]].append(evt[1])
            T = max(T,evt[1])
        qua_table = []
        for t in range(1,T):
            for end in evt_dic[t] : heapq.heappush(qua_table,end)
            while qua_table and qua_table[0]<t: heapq.heappop(qua_table)
            if qua_table:
                ans += 1
                heapq.heappop(qua_table)
        return ans







