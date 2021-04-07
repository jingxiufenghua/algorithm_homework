# 剑指 Offer 16. 数值的整数次方
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if x == 0 : return 1
        # res = 1
        # for i in range(abs(n)):
        #     res = res*x
        # return res  if n>0 else 1/res

        if x == 0 : return 0
        res = 1
        if n<0: x,n = 1/x,-n
        while n:
            if n&1:
                res *= x
            x *=x
            n>>=1
        return res
