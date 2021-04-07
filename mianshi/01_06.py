# 面试题 01.06. 字符串压缩
import collections
class Solution:
    def compressString(self, S: str) -> str:
        if not S : return ""
        ans = ""
        temp = 1
        cnt = 0
        ch = S[0]
        for c in S:
            if c == ch:
                cnt +=1
            else:
                ans += ch + str(cnt)
                ch = c
                cnt = 1
        ans += ch + str(cnt)
        return ans if len(ans) < len(S) else S



        return res

solution = Solution()
string = "abbccd"
result = solution.compressString(string)
print(result)