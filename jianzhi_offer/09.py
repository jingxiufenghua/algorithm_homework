class CQueue:

    def __init__(self):
        self.A = []
        self.B = []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A : return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()





# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
# obj = CQueue()
# obj.appendTail(3)


class CQueue:

    def __init__(self):
        self.first = []
        self.second = []

    def appendTail(self, value: int) -> None:
        self.first.append(value)
    def deleteHead(self) -> int:
        if self.second: self.second.pop()
        if not self.first: return -1
        while self.first:
            self.second.append(self.first.pop())
        return  self.second.pop()

# Your CQueue object will be instantiated and called as such:
obj = CQueue()

opr = ["deleteHead","appendTail","deleteHead","appendTail","appendTail","deleteHead","deleteHead","deleteHead","appendTail","deleteHead","appendTail","appendTail","appendTail","appendTail","appendTail","appendTail","deleteHead","deleteHead","deleteHead","deleteHead"]
val = [[],[12],[],[10],[9],[],[],[],[20],[],[1],[8],[20],[1],[11],[2],[],[],[],[]]

for i in range(len(opr)):
    if opr[i] == "deleteHead":
        print(obj.deleteHead())
    elif opr[i] == "appendTail":
        print(obj.appendTail(val[i]))