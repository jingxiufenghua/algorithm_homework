#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：gaopingtimu.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/24 12:43 
'''
from typing import List
# 146. LRU 缓存机制
class DLinkednode:
    def __init__(self,key = 0,value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DLinkednode()
        self.tail = DLinkednode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkednode(key,value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size>self.capacity:
                node = self.removeTail()
                self.cache.pop(node.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next


    def moveToHead(self,node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

solution = LRUCache(2)
solution.put(1,1)
solution.put(2,2)
solution.get(1)
solution.put(3,3)
solution.get(2)
solution.put(4,4)
solution.get(1)
solution.get(3)
solution.get(4)



