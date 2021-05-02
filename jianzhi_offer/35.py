#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：35.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/1 16:10 
'''
# 剑指 Offer 35. 复杂链表的复制
from typing import List
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # 复制简单链表
    def copyList(self, head: 'Node') -> 'Node':
        if not head:return Node
        cur = head
        dum = pre = Node(0)
        while cur:
            node = Node(cur.val)
            pre.next = node
            cur = cur.next
            pre = node
        return dum.next
    # 复制复杂链表
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head : return None
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]





