import collections
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hash_map = collections.Counter(nums)
        for k,v in hash_map.items():
            if v>2:
                return k