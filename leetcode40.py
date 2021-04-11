# 40. 组合总和 II
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(nowindex,nowlist,nowans):
            if nowans == target:
                ans.append(nowlist)
                return
            for i in range(nowindex,len(candidates)):
                if nowans + candidates[i]>target:
                    break
                if i>0 and i>nowindex and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1,nowlist+[candidates[i]],nowans+candidates[i])
        dfs(0,[],0)
        return ans
