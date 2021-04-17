from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n):
            if i >= n-i-1:
                break
            s[i],s[n-i-1] = s[n-i-1],s[i]

solution = Solution()
s  = ["h","e","l","l","o"]
result =  solution.reverseString(s)

