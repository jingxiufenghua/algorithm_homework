# 面试题 01.02. 判定是否互为字符重排
import collections
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        hash_s1 = collections.Counter(s1)
        hash_s2 = collections.Counter(s2)

        if len(hash_s2)!=len(hash_s1):
            return False

        for k,v in hash_s1.items():
            if k not in hash_s2:
                return False
            elif v != hash_s2[k]:
                return False
        return True



