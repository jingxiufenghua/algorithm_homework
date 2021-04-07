# 面试题 01.04. 回文排列
import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s: return False
        hash_map = collections.Counter(s)
        res = 0
        for k,v in hash_map.items():
            if v % 2 !=0:
                res += 1
                if res>1:
                    return False
        return True
