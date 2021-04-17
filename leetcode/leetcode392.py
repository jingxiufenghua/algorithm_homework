class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m,n = len(s),len(t)
        if m>n:return False
        res = []
        temp = 0
        for i in range(m):
            for j in range(temp,n):
                if s[i] == t[j]:
                    res.append(s[i])
                    temp = j+1
                    break
        return len(s) == len(res)