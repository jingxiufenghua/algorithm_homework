#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：02.03.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 16:26 
'''
from typing import List
# 面试题 02.03. 删除中间节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
