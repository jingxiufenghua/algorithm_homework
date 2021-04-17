# 剑指 Offer 47. 礼物的最大价值
from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # def dfs(i,j):
        #     if not 0<=i<len(grid) or not 0<=j<len(grid[0]):return []
        #     res.append(grid[i][j])
        #     down = grid[i+1][j] if i<len(grid)-1 else -1
        #     right = grid[i][j+1] if j<len(grid[0])-1 else -1
        #     if down > right:
        #         dfs(i+1,j)
        #     else:
        #         dfs(i,j+1)
        #
        # res = []
        # dfs(0,0)
        # return sum(res)

        n,m = len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if i==0 and j==0: continue
                if i == 0: grid[i][j] += grid[i][j-1]
                elif j == 0: grid[i][j] += grid[i-1][j]
                else:  grid[i][j] += max(grid[i-1][j],grid[i][j-1])  # i!=0 and j!=0
        return grid[-1][-1]

solution = Solution()
nums = [[1,2,5],[3,2,1]]
result = solution.maxValue(nums)
print(result)


