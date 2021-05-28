from typing import List
# class Solution:
#     def dfs(self,grid,r,c):
#         grid[r][c] = 0 # 重要
#         nr,nc = len(grid),len(grid[0])
#         for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
#             if 0<=x<nr and 0<=y<nc and grid[x][y]=="1":
#                 self.dfs(grid,x,y)
#
#     def numIslands(self, grid: List[List[str]]) -> int:
#         nr = len(grid)
#         if nr==0:return 0
#         nc = len(grid[0])
#         num_islands = 0
#         for r in range(nr):
#             for c in range(nc):
#                 if grid[r][c] == "1":
#                     num_islands +=1
#                     self.dfs(grid,r,c)
#         return num_islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr==0:return 0
        nc = len(grid[0])
        num_island = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    num_island += 1
                    self.dfs(grid,i,j)
        return num_island
    def dfs(self,grid,r,c):
        grid[r][c] = 0
        nr,nc = len(grid),len(grid[0])
        for x,y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if 0<=x<nr and 0<=y<nc and grid[x][y] == "1":
                self.dfs(grid,x,y)



solution = Solution()
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
result = solution.numIslands(grid)
print(result)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0: return 0
        nc = len(grid[0])
        numland = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    numland += 1
                    self.dfs(grid,i,j)
        return numland
    def dfs(self,grid,i,j):
        grid[i][j] = 0
        nr = len(grid)
        nc = len(grid[0])
        for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0<=x<nr and 0<=y<nc and grid[x][y] == "1":
                self.dfs(grid,x,y)

