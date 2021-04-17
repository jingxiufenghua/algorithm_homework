# 剑指 Offer 58 - I. 翻转单词顺序
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return ""
        string = s.strip(" ")
        word_list = string.split()
        res = ""
        for i in range(len(word_list)-1,-1,-1):
            res += word_list[i] + " "
        return res.rstrip(" ")
solution = Solution()
s = "a good   example"
temp = "blue is sky the"
result = solution.reverseWords(s)
print(result)
print(result == temp)
