import math
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [math.inf]
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x,self.min_stack[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]

minStack = MinStack()
print(minStack.push(2))
print(minStack.push(0))
print(minStack.push(3))
print(minStack.push(0))
print(minStack.getMin())  # --> 返回 -3.
print(minStack.pop())
print(minStack.getMin())  # --> 返回 -3.
print(minStack.pop())
print(minStack.getMin())  # --> 返回 -3.
print(minStack.pop())
print(minStack.getMin())  # --> 返回 -3.


