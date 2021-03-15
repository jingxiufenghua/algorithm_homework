class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4!=0

solution = Solution()
num = 7
result = solution.canWinNim(num)
print(result)
