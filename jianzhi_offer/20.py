# 剑指 Offer 20. 表示数值的字符串
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            a = float(s)
        except:
            return False
        else:
            return True