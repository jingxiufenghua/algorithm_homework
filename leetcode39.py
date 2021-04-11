# 39. 组合总和
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
from typing import List
class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     ans = set()
    #     def dfs(now,nowlist):
    #         if now==target:
    #             nowlist.sort()
    #             tuplelist = tuple(nowlist)
    #             if tuplelist not in ans:
    #                 ans.add(tuplelist)
    #         if now>target:
    #             return
    #         for i in range(len(candidates)):
    #             dfs(now+[candidates[i]],nowlist+candidates[i])
    #     dfs(0,[])
    #     return list(ans)




    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     ans = []
    #     def dfs(nowindex,nowlist,nowans):
    #         if nowans == target:
    #             ans.append(nowlist)
    #             return
    #         if nowans>target:
    #             return
    #         for i in range(nowindex,len(candidates)):
    #             dfs(i,nowlist+[candidates[i]],nowans+candidates[i])
    #     dfs(0,[],0)
    #     return ans

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(nowindex, nowlist, nowans):
            if nowans == target:
                ans.append(nowlist)
                return
            if nowans > target:
                return
            for i in range(nowindex, len(candidates)):
                if nowans + candidates[i] > target:
                    break
                dfs(i, nowlist + [candidates[i]], nowans + candidates[i])
        dfs(0, [], 0)
        return ans




