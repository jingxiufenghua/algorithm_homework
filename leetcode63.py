from  typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 0
                else:
                    if i==j==0:
                        obstacleGrid[i][j] = 1
                    else:
                        a = obstacleGrid[i-1][j] if i!=0 else 0
                        b = obstacleGrid[i][j-1] if j != 0 else 0
                        obstacleGrid[i][j] = a+b
                print("i:%d,j:%d,obstacleGrid:"%(i,j),obstacleGrid)
        return obstacleGrid[-1][-1]
solution = Solution()
obstacleGrid = [[0,0],[1,1],[0,0]]
result = solution.uniquePathsWithObstacles(obstacleGrid)
print(result)


