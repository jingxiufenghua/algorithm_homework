#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：59_II.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/28 16:49 
'''
# 剑指 Offer 59 - II. 队列的最大值
from typing import List
import numpy as np
class MaxQueue:

    def __init__(self):
        self.A = []
        self.B = []
        self.max = -np.inf

    def max_value(self) -> int:
        if not self.A and not self.B:
            return -1
        else:
            self.max = max(self.A+self.B)
            return self.max
    def push_back(self, value: int) -> None:
        self.A.append(value)

    def pop_front(self) -> int:
        if self.B:
            return self.B.pop()
        elif not self.B and not self.A :
            return -1
        else:
            while self.A:
                self.B.append(self.A.pop())
            return self.B.pop()

import queue
class MaxQueue:

    def __init__(self):
        self.deque = queue.deque()

    def max_value(self) -> int:
        return max(self.deque) if self.deque else -1

    def push_back(self, value: int) -> None:
        self.deque.append(value)

    def pop_front(self) -> int:
        return self.deque.popleft() if self.deque else -1




# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
