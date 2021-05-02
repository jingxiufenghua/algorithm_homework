#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：237_week_compitition.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/18 10:28 
'''
from typing import List
import collections
# class Solution:
#     def checkIfPangram(self, sentence: str) -> bool:
#         dict = collections.Counter(sentence)
#         return len(dict)==26

# class Solution:
#     def maxIceCream(self, costs: List[int], coins: int) -> int:
#         costs.sort()
#         sum = 0
#         res = []
#         for i in range(len(costs)):
#             if sum + costs[i]<k:
#                 sum += costs
#                 res.append(costs[i])
#         return len(res)



from typing import List
import heapq
# class Solution:
# 超时
    # def getOrder(self, tasks: List[List[int]]) -> List[int]:
    #     n = len(tasks)
    #     res = []
    #     wait_list = []
    #     tasks = sorted(list(enumerate(tasks)),key=lambda x: x[1][0])
    #     times = tasks[0][1][0]
    #     i,j = 0,0
    #     while i<n:
    #         while j<n and tasks[j][1][0]<=times:
    #             wait_list.append((tasks[j][0],tasks[j][1][1]))
    #             j += 1
    #         wait_list.sort(key=lambda x : (x[1],x[0]))
    #         res.append(wait_list[0][0])
    #         times += wait_list[0][1]
    #         i += 1
    #         del wait_list[0]
    #     return res

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted(enumerate(tasks), key=lambda x: (-x[1][0],-x[1][1],-x[0])) # 多键值排序
        print(tasks)
        ans = []
        pq = []
        time = 0
        while tasks or pq:
            if pq:
                l, idx, t = heapq.heappop(pq)
                ans.append(idx)
            else:
                idx, v = tasks.pop()
                ans.append(idx)
                t, l = v
            time = max(t,time) + l  # 这个地方处理的非常好 t 和 time 取最大值
            while tasks and tasks[-1][1][0] <= time:
                index, val = tasks.pop()
                ti, le = val
                heapq.heappush(pq, (le, index, ti))
        return ans


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indices = list(range(n))
        indices.sort(key=lambda x: tasks[x][0])

        ans = list()
        # 优先队列
        q = list()
        # 时间戳
        timestamp = 0
        # 数组上遍历的指针
        ptr = 0

        for i in range(n):
            # 如果没有可以执行的任务，直接快进
            if not q:
                timestamp = max(timestamp, tasks[indices[ptr]][0])
            # 将所有小于等于时间戳的任务放入优先队列
            while ptr < n and tasks[indices[ptr]][0] <= timestamp:
                heapq.heappush(q, (tasks[indices[ptr]][1], indices[ptr]))
                ptr += 1
            # 选择处理时间最小的任务
            process, index = heapq.heappop(q)
            timestamp += process
            ans.append(index)

        return ans

solution = Solution()
nums = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
result = solution.getOrder(nums)
print(result)