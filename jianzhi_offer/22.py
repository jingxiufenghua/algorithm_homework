#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：22.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/28 17:41 
'''
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        cur,second = head,head
        while k>0:
            second = second.next
            k -= 1
        while second:
            second = second.next
            cur = cur.next
        return cur

