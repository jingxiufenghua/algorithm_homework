#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：52.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/27 23:57 
'''
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB :return None
        sava_A,save_B = headA,headB
        while headA or headB:
            if not headA:
                headA = save_B
            if not headB:
                headB = sava_A
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1


作者：z1m
链接：https: // leetcode - cn.com / problems / liang - ge - lian - biao - de - di - yi - ge - gong - gong - jie - dian - lcof / solution / shuang - zhi - zhen - fa - lang - man - xiang - yu - by - ml - zimingm /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。