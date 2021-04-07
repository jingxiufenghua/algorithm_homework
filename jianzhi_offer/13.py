class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def dfs(i,j,k,matrix):
            if not 0<=i<m or not 0<=j<n or matrix[i][j]>k: return False
            if matrix[i][j]<= k:
                matrix[i][j] = k+1
            return 1 + dfs(i+1,j,k,matrix) + dfs(i,j+1,k,matrix)
        def make_list(n):
            list = []
            while n > 0:
                list.append(n % 10)
                n = n // 10
            return list
        matrix = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                matrix[i][j] = sum(make_list(i)) + sum(make_list(j))
        return  dfs(0,0,k,matrix)

solution = Solution()
m = 2
n = 3
k = 1
result = solution.movingCount(m,n,k)
print(result)


