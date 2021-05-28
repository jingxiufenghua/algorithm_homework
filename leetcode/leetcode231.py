# 2的幂
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

solution = Solution()
n = 12
result = solution.isPowerOfTwo(n)
print(result)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1)==0