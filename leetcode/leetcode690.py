#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode690.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/1 12:17 
'''
from typing import List
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees.sort(key = lambda x:x.id)
        ans = 0
        for item in employees:
            if item.id == id :
                ans += item.importance
                break
        def sub_sum(item,ans):
            for sub in employees:
                if sub.id in item.subordinates:
                    ans += sub.importance
                    ans = sub_sum(sub,ans)
            return ans
        ans = sub_sum(item,ans)
        return ans
solution = Solution()
employees1 = Employee(1,5,[2,3])
employees2 = Employee(2,3,[4])
employees3 = Employee(3,4,[])
employees4 = Employee(4,1,[])
employees = [employees1,employees2,employees3,employees4]
result = solution.getImportance(employees,1)
print(result)




