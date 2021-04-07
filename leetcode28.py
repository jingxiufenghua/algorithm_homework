class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
solution = Solution()
str1 ="hello"
str2 ="ll"
ListNode1 = solution.strStr(str1,str2)
print(ListNode1)


# KMP
class Solution:
    def get_next(self,s:str):
        j = 0
        n = len(s)
        next = [0]*(n+1)
        for i in range(1,n):
            while j>0 and s[i] != s[j]:
                j = next[j-1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
        return next

    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if not needle:return 0
        next = self.get_next(needle)
        j = 0
        for i in range(len(haystack)):
            while j>0 and haystack[i] != needle[j]:
                j = next[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return i-n +1
        return -1

