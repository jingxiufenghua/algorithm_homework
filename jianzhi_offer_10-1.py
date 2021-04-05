# class Solution:
#     def fib(self, n: int) -> int:
#         f = [0]*(n+1)
#         if n == 0 : return 0
#         if n == 1 : return 1
#         f[0] = 0
#         f[1] = 1
#         for i in range(2,n+1):
#             f[i] = f[i-1] + f[i-2]
#         # return int(f[n]%(1e9+7))
#         return  f[n]%1000000007
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

solution = Solution()
n = 4
result = solution.fib(n)
print(result)