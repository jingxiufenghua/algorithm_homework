
class StockSpanner(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight

# Your StockSpanner object will be instantiated and called as such:
S= StockSpanner()
param_1 = S.next(100)
print(param_1)
param_1 = S.next(80)
print(param_1)
param_1 = S.next(60)
print(param_1)
param_1 = S.next(70)
print(param_1)
param_1 = S.next(60)
print(param_1)
param_1 = S.next(75)
print(param_1)
param_1 = S.next(85)
print(param_1)


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price,weight))
        return weight


