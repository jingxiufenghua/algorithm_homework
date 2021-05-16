# 40. 组合总和 II
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
from typing import List
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         ans = []
#         def dfs(nowindex,nowlist,nowans):
#             if nowans == target:
#                 ans.append(nowlist)
#                 return
#             for i in range(nowindex,len(candidates)):
#                 if nowans + candidates[i]>target:
#                     break
#                 if i>0 and i>nowindex and candidates[i] == candidates[i-1]:
# 上一句代码的详解 https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/225211/
#                     continue
#                 dfs(i+1,nowlist+[candidates[i]],nowans+candidates[i])
#         dfs(0,[],0)
#         return ans


# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         n = len(candidates)
#         candidates.sort()
#         def dfs(nums,index,temp):
#             if index == n:
#                 return
#             temp = temp[:]
#             for i in range(index,n):
#                 temp.append(candidates[i])
#                 if sum(temp) == target and temp not in res:
#                     res.append(temp[:])
#                 elif sum(temp)>target:
#                     break
#                 dfs(nums,i+1,temp)
#                 temp.pop()
#         res = []
#         dfs(candidates,0,[])
#         return res

# import collections
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         def dfs(pos: int, rest: int):
#             nonlocal sequence
#             if rest == 0:
#                 ans.append(sequence[:])
#                 return
#             if pos == len(freq) or rest < freq[pos][0]:
#                 return
#
#             dfs(pos + 1, rest)
#
#             most = min(rest // freq[pos][0], freq[pos][1])
#             for i in range(1, most + 1):
#                 sequence.append(freq[pos][0])
#                 dfs(pos + 1, rest - i * freq[pos][0])
#             sequence = sequence[:-most]
#
#         freq = sorted(collections.Counter(candidates).items())
#         ans = list()
#         sequence = list()
#         dfs(0, target)
#         return ans

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        n = len(candidates)
        if n == 0: return []
        def dfs(index,nowlist,nowans):
            if nowans == target:
                ans.append(nowlist)
                return
            for i in range(index,n):
                if nowans + candidates[i] >target:
                    break
                if i>index and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1,nowlist + [candidates[i]],nowans+candidates[i])
        dfs(0,[],0)
        return ans



solution = Solution()
candidates = [2,5,2,1,2]
target = 7
result = solution.combinationSum2(candidates,target)
print(result)
