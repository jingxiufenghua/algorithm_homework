#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode203.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/3 22:52 
'''
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        dummy = ListNode()
        cur = dummy
        dummy.next = head
        while cur:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return dummy.next

