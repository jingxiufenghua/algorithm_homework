# 剑指 Offer 41. 数据流中的中位数
# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = len(self.stack)


    def addNum(self, num: int) -> None:
        self.stack.append(num)
        self.size +=1


    def findMedian(self) -> float:
        if self.size&1 == 1:
            return self.stack[self.size>>1]
        else:
            return (self.stack[self.size>>1-1] + self.stack[self.size>>1])>>1



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(num)
param_2 = obj.findMedian()
