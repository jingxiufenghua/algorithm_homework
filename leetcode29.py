class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = -1 if(dividend>0 and divisor<0) or (dividend<0 and divisor>0) else 1
        dividend,divisor = abs(dividend),abs(divisor)
        q,times = 0,0
        while dividend>= divisor:
            cur = dividend - (divisor<<times)
            if cur>=0:
                q+=(1<<times)
                times +=1
                dividend = cur
            else:
                times-=1
        return max(-2**31,min(q*flag,2**31-1))

class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:
        limit = 2**31
        isNeg = (dividend<0)!=(divisor<0)
        dividend,divisor = abs(dividend),abs(divisor)
        res = 0
        div,track = divisor,1
        while dividend>=divisor:
            while dividend>=(div<<1):
                div<<=1
                track<<=1
            res += track
            dividend -= div
            div,track = divisor,1
        return max(-limit,min(limit-1,-res if isNeg else res))
solution = Solution2()
solution.divide(-2147483648,-1)


