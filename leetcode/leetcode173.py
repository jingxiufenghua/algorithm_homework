#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode173.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/28 18:04 
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import  collections
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.deque = collections.deque()
        self.inorder(root)


    def inorder(self,root):
        if not root:return
        self.inorder(root.left)
        self.deque.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        return self.deque.popleft()

    def hasNext(self) -> bool:
        return len(self.deque)>0

