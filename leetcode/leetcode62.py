class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     f = [[1]*n]+[[1]+[0]*(n-1) for _ in range(m-1)]
    #     for i in range(1,m):
    #         for j in range(1,n):
    #             f[i][j] = f[i-1][j] + f[i][j-1]
    #     return f[m-1][n-1]

    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                cur[j] += cur[j-1]
        return cur[n-1]



solution = Solution()
m = 3
n = 2
result = solution.uniquePaths(m,n)
print(result)




