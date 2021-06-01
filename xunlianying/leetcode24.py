#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode24.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/6/1 9:57 
'''
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# 24. 两两交换链表中的节点
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre,pre.next = self,head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next,b.next,a.next = b,a,b.next
            pre = a
        return self.next

# 206
# 反转链表  最强精简版
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur,prev = head,None
        while cur:
            cur.next,prev,cur = prev,cur,cur.next
        return prev
# 141. 环形链表
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
