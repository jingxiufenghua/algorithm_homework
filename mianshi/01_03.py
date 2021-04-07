# 面试题 01.03. URL化
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        res = ""
        replace_str = "%20"
        for i in range(length):
            if S[i] == " ":
                res +=replace_str
            else:
                res += S[i]

        return res

