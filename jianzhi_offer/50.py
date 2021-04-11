import collections
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:return ""
        hash_map = collections.Counter(s)
        for k,v in hash_map.items():
            if v <2:
                return k
        return " "