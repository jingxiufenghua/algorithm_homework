from  typing import List
import numpy as np
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        key = cmp_to_key(lambda x, y: int(y+x) - int(x+y))
        res = ''.join(sorted(map(str, nums), key=key)).lstrip('0')
        return res or '0'
solution = Solution()
result = solution.largestNumber([3,30,34,5,9])
print(result)












