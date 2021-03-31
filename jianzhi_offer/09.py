class CQueue:

    def __init__(self):
        self.stack = []
        self.res = []


    def appendTail(self, value: int) -> None:
        self.stack.append(value)
        self.res.append(len(self.stack))

    def deleteHead(self) -> int:




# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
obj = CQueue()
obj.appendTail(3)
