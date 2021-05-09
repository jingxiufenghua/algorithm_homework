#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：02.06.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 16:33 
'''
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        n = len(res)
        return res[:n//2] == res[n//2+1:] if n&1 == 1 else res[:n//2] == res[n//2:]