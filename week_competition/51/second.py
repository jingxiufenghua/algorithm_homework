#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：second.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/1 22:14 
'''
# import heapq
# from typing import List
# class SeatManager:
#
#     def __init__(self, n: int):
#         self.reserve_list = [i for i in range(1,n+1)]
#         heapq.heapify(self.reserve_list)
#
#
#     def reserve(self) -> int:
#         return heapq.heappop(self.reserve_list)
#
#     def unreserve(self, seatNumber: int) -> None:
#         heapq.heappush(self.reserve_list,seatNumber)

from sortedcontainers import SortedList
class SeatManager:
    def __init__(self, n: int):
        self.order = SortedList([i for i in range(1,n+1)])

    def reserve(self) -> int:
        return self.order.pop(0)

    def unreserve(self, seatNumber: int) -> None:
        self.order.add(seatNumber)



# import collections
# class SeatManager:
#     def __init__(self, n: int):
#         self.hash_map = collections.OrderedDict()
#         for i in range(1,n+1):
#             self.hash_map[i] = 0
#
#     def reserve(self) -> int:
#         for k,v in self.hash_map.item():
#             if v == 0 :
#                 self.hash_map[k] = 1
#                 break
#
#     def unreserve(self, seatNumber: int) -> None:
#         self.hash_map[seatNumber] = 0

# Your SeatManager object will be instantiated and called as such:
obj = SeatManager(5)
print(obj.reserve())
print(obj.reserve())
print(obj.unreserve(2))
print(obj.reserve())
print(obj.reserve())
print(obj.reserve())
print(obj.reserve())
