# 5722. 截断句子
# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         if not s: return ""
#         words = s.split(" ")
#         res = ""
#         for i in range(k):
#             res = res+words[i] + " "
#         return  res.rstrip(" ")
# solution = Solution()
# s = "Hello how are you Contestant"
# result = solution.truncateSentence(s,4)
# print(result)
from typing import List
# class Solution:
#     def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
#         n = len(logs)
#         hash_map = dict()
#         res = {}
#         answer = {}
#         result = []
#         for log in logs:
#             user = log[0]
#             time = log[1]
#             if user not in hash_map:
#                 hash_map.setdefault(user,[])
#                 hash_map[user].append(time)
#                 res[user]=1
#             else:
#                 if time not in hash_map[user]:
#                     hash_map[user].append(time)
#                     res[user] +=1
#         for i in range(1,k+1):
#             answer.setdefault(i,0)
#
#         for k,v in res.items():
#             if v in answer:
#                 answer[v] +=1
#
#         for k,v in answer.items():
#             result.append(v)
#         return result
# import collections
# class Solution:
#     def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
#         d = collections.defaultdict(list)
#         for i in range(len(logs)):
#             d[logs[i][0]].append(logs[i][1])
#         ans = [0]*k
#         for i in d:
#             d[i] = len(set(d[i]))
#         for i in d:
#             ans[d[i]-1]+=1
#         return ans

# solution = Solution()
# logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
# result = solution.findingUsersActiveMinutes(logs,4)
# print(result)

#5724
# import numpy as np
# class Solution:
#     def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
#         n = len(nums1)
#         less = 0
#         diff = [abs(nums1[i]-nums2[i]) for i in range(n)]
#         sum_diff = sum(diff)%(1e9+7)
#         change_id = np.argmax(diff)
#         min_elem_index = change_id
#         for i in range(n):
#             if abs(nums1[i]-nums2[change_id])<abs(nums1[min_elem_index]-nums2[change_id]):
#                 min_elem_index = i
#         nums1[change_id] = nums1[min_elem_index]
#         diff = [abs(nums1[i]-nums2[i]) for i in range(n)]
#         sum_diff = sum(diff)%(1e9+7)
#         return sum_diff

# 1688. 比赛中的配对次数
# class Solution:
#     def numberOfMatches(self, n: int) -> int:
#         res = []
#         while n>=2:
#             rest = n%2
#             res.append(n // 2)
#             if rest==0:
#                 n=n//2
#             else:
#                 n = n//2+1
#         return sum(res)


# 1689. 十-二进制数的最少数目
class Solution:
    def minPartitions(self, n: str) -> int:
        # nums = []
        # another = [int(v) for v in n]
        # temp = ""
        # while len(another)>0:
        #     for i in range(len(another)):
        #         if another[i]>0:
        #             temp = temp + "1"
        #             another[i] =  another[i]-1
        #         else:
        #             temp = temp + "0"
        #     nums.append(temp)
        #     temp = ""
        #
        #     while len(another)>0:
        #         if another[0]!=0:
        #             break
        #         another.remove(another[0])
        # return len(nums)

        return int(max(n))

solution = Solution()
str1 = "32"
result = solution.minPartitions(str1)
print(result)

# 1690. 石子游戏 VII
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:








