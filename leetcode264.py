# 264. 丑数 II
# 超出时间限制
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         def isUglyNumber(n):
#             if n<=0:
#                 return False
#             factors = [2,3,5]
#             for factor in factors:
#                 while n%factor == 0:
#                     n //=factor
#             return n==1
#         count = 0
#         i = 1
#         while count<n:
#             if isUglyNumber(i):
#                 count += 1
#             i += 1
#         return  i-1

class Solution:
    def nthUglyNumber(self, n: int) -> int:

