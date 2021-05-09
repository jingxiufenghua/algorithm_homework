#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：02.08.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 17:42 
'''
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:return None
        cur = head
        dict = set()
        while cur :
            if cur not in dict:
                dict.add(cur)
            else:
                return cur
            cur = cur.next
        return
