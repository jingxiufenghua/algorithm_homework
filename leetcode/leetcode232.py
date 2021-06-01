#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode232.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/6/1 15:18 
'''
from typing import List
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_a = []
        self.stack_b = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_a.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack_b:
            return self.stack_b.pop()
        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack_b:
            return self.stack_b[-1]
        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())
        return self.stack_b[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack_a) + len(self.stack_b) == 0:
            return True
        else:
            return False

