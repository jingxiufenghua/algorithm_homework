import heapq

# class Solution:
#     def magicTower(self, nums):
#         if sum(nums)<0:
#             return -1
#         hurts = []
#         blood = 0
#         counts = 0
#         heapq.heapify(hurts)
#         for i in nums:
#             blood += i
#             if i<0:heapq.heappush(hurts,i)
#             if blood<0:
#                 counts += 1
#                 blood -= heapq.heappop(hurts)
#         return counts

# 5717. 最少操作使数组递增
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1 : return 0
#         i = 0
#         count = 0
#         while i<n-1:
#             if nums[i]>=nums[i+1]:
#                 count += nums[i] - nums[i+1]+1
#                 nums[i+1] = nums[i]+1
#             i += 1
#         return count
# 5718. 统计一个圆中点的数目
from  typing import  List
# class Solution:
#     def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
#         res = []
#         for (x1,y1,r1) in range(len(queries)):
#             count = 0
#             for (x2,y2) in points:
#                 if (x1-x2)**2 + (y1-y2)**2<=r1**2:
#                     count+=1
#             res.append(count)
#         return res

# 5719. 每个查询的最大异或值
import math
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # n = len(nums)
        # K = int(math.pow(2,maximumBit)-1)
        # res = []
        # while nums:
        #     XOR = nums[0]
        #     for i in range(1,len(nums)):
        #         XOR ^= nums[i]
        #     XOR ^= K
        #     res.append(XOR)
        #     nums.pop()
        # return res
#
#         n = len(nums)
#         K = int(math.pow(2,maximumBit)-1)
#         res = []
#         XOR = nums[0]
#         for i in range(1,n):
#             XOR ^=nums[i]
#         while nums:
#             res.append(XOR^K)
#             XOR ^= nums.pop()
#         return res
#
#
#
# solution = Solution()
# nums = [0,1,1,3]
# result = solution.getMaximumXor(nums,2)
# print(result)


# 5720. 使字符串有序的最少操作次数
class Solution:
    def makeStringSorted(self, s: str) -> int:
        n = len(s)
        if n == 1: return 0
        word_list = [ord(s[i])  for i in range(n)]
        for i in range(n):
            if word_list[i]<word_list[i-1]:
                break