#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：62.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/28 14:33 
'''
from typing import List
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        list = [i for i in range(n)]
        index = 0
        while len(list)>1:
            id = (index+m-1)%len(list)
            del list[id]
            index = id

        return list[0]

# class Solution {
# public:
#     int lastRemaining(int n, int m) {
#         int pos = 0; // 最终活下来那个人的初始位置
#         for(int i = 2; i <= n; i++){
#             pos = (pos + m) % i;  // 每次循环右移
#         }
#         return pos;
#     }
# };
#
# 作者：aspenstarss
# 链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/huan-ge-jiao-du-ju-li-jie-jue-yue-se-fu-huan-by-as/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。