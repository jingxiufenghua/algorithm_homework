# 剑指 Offer 10- II. 青蛙跳台阶问题
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0 or n==1: return 1
        f = [0]*(n+1)
        f[0] = 1
        f[1] = 1
        i = 2
        while i<=n:
            f[i] = f[i-1] + f[i-2]
            i += 1
        return f[i-1]%1000000007

solution = Solution()
n = 2
result = solution.numWays(n)
print(result)
