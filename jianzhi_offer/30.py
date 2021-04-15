class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.compare = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.compare or self.compare[-1]>=x:
            self.compare.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.compare[-1]:
            self.compare.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.compare.[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()