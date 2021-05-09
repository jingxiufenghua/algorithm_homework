#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：02.01.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 11:59 
'''
from typing import List
# 面试题 02.01. 移除重复节点
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:return None
        dummy = ListNode(0)
        dummy.next,cur = head,head
        res = []
        while cur:
            if cur.val not in res:
                res.append(cur.val)
            if cur.next and cur.next.val in res:
                cur.next = cur.next.next
                continue
            cur = cur.next
        return dummy.next

