from typing import List
# 5698. 构成特定和需要添加的最少元素
'''
给你一个整数数组 nums ，和两个整数 limit 与 goal 。数组 nums 有一条重要属性：abs(nums[i]) <= limit 。

返回使数组元素总和等于 goal 所需要向数组中添加的 最少元素数量 ，添加元素 不应改变 数组中 abs(nums[i]) <= limit 这一属性。

注意，如果 x >= 0 ，那么 abs(x) 等于 x ；否则，等于 -x 。
'''
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        list_sum = sum(nums)
        diff = goal - list_sum
        diff_abs = abs(goal-list_sum)
        if diff_abs==0: return 0
        if diff_abs<=limit and diff_abs>0:return 1
        count = diff_abs//limit
        diff_abs = diff_abs - count*limit
        if diff_abs==0 : return count
        return count+1
solution = Solution()
goal = 6
limit = 300
nums = [1,2,3]
result = solution.minElements(nums,limit,goal)
print(result)

# 5681. 判断一个数字是否可以表示成三的幂的和
"""
给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。

对于一个整数 y ，如果存在整数 x 满足 y == 3x ，我们称这个整数 y 是三的幂。
"""
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
























# 5697
# class Solution:
#     def checkOnesSegment(self, s: str) -> bool:
#         if  not s :return False
#         s = list(s)
#         count = 0
#         for i in range(len(s)-1,0,-1):
#             if s[i] == "1":
#                 count +=1
#             if s[i] == "0" and count>0:
#                 return False
#         return True
# solution = Solution()
# s = "1"
# result = solution.checkOnesSegment(s)
# print(result)































# class Solution:
#     def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
#         n = len(points)
#         distance = -1
#         res = -1
#         for i in range(n):
#             x1 = points[i][0]
#             y1 = points[i][1]
#             if x1 == x or y1 == y:
#                 if distance < 0:
#                     distance = abs(points[i][0]-x) + abs(points[i][1]-y)
#                     res = i
#                 else:
#                     if distance==abs(points[i][0]-x) + abs(points[i][1]-y):
#                         if points[res][0] + points[res][1] > points[i][0] + points[i][1]:
#                             res = i
#                     elif distance>abs(points[i][0]-x) + abs(points[i][1]-y):
#                         distance = abs(points[i][0]-x) + abs(points[i][1]-y)
#                         res = i
#         return res
#
# solution = Solution()
# x = 3
# y = 4
# points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
# result = solution.nearestValidPoint(x,y,points)
# print(result)
# dogdistance = {'dog-dog': 33, 'dog-cat': 33, 'dog-car': 41, 'dog-bird': 42}
# print(min(dogdistance, key=dogdistance.get))