class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk,ans = -1,0
        for i in range(n):
            if i!=0:
                occ.remove(s[i-1])
            while rk+1<n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans,rk-i+1)
        return ans



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        left,right = 0,0
        length = 0
        while right<n:
            while s[right] in occ:
                occ.remove(s[left])
                left += 1
            occ.add(s[right])
            length = max(length, len(occ))
            right += 1
        return length

solution = Solution()
s = " "
result = solution.lengthOfLongestSubstring(s)
print(result)


