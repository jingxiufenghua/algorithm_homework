#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：02.05.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 15:00 
'''
from typing import List
# 面试题 02.05. 链表求和
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        cur1,cur2 = l1,l2
        dummy = cur = ListNode(0)
        temp = 0
        while cur1 and cur2:
            cur.next = ListNode((cur1.val + cur2.val+temp)%10)
            temp = (cur1.val + cur2.val)//10
            cur1 = cur1.next
            cur2 = cur2.next
            cur = cur.next
            if cur1 and not cur2: cur2 = ListNode(0)
            if not cur1 and cur2: cur1 = ListNode(0)
        while temp>0:
            cur.next = ListNode(temp%10)
            cur = cur.next
        return dummy.next




