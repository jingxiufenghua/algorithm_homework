import collections
class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     bin_array =  str(bin(n))[2:]
    #     hash_map = collections.Counter(bin_array)
    #     return hash_map["1"]

    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n&1
            n>>=1
        return res
solution = Solution()
n = 2
result = solution.hammingWeight(n)
print(result)
