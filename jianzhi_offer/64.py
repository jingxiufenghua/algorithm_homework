# 剑指 Offer 64.
# 求1+2+…+n求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# python的 and 操作如果最后结果为真，返回最后一个表达式的值，or 操作如果结果为真，返回第一个结果为真的表达式的值
class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n-1))