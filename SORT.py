from typing import List
class Solution:
    def  bubbleSort(self, nums: List[int]) -> List[int]:
        if not nums : return False
        n = len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j+1]<nums[j]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums

    def selectionSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            minindex = i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[minindex]:
                    minindex = j
            nums[i],nums[minindex] = nums[minindex],nums[i]
        return nums

    def insertionSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            curNum,preIndex = nums[i+1],i
            while preIndex>=0 and curNum<nums[preIndex]:
                nums[preIndex+1] = nums[preIndex]
                preIndex -=1
            nums[preIndex+1] = curNum
        return nums

    def mergeSort(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            result = []
            i=j=0
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            result = result + left[i:] + right[j:]
            return result

        if len(nums)<=1:return nums
        mid = len(nums)//2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return merge(left,right)

    def quickSort(self, nums: List[int]) -> List[int]:
        """
        :param nums:
        :return:
        """
        if len(nums)<=1: return nums
        pivot = nums[0]
        left = [nums[i] for i in range(1,len(nums)) if nums[i]<pivot]
        right = [nums[j] for j in range(1,len(nums)) if nums[j]>=pivot]
        return self.quickSort(left) + [pivot] + self.quickSort(right)

    def quickSort2(self, nums: List[int],left,right) -> List[int]:
        def partiton(nums,left,right):
            pivot = nums[left]
            while left<right:
                while left<right and nums[right]>=pivot:
                    right -=1
                nums[right] = nums[left]
                while left<right and nums[left]<pivot:
                    left +=1
                nums[right] = nums[left]
            nums[left] = pivot
            return left
        if left<right:
            pivotIndex = partiton(nums,left,right)
            self.quickSort2(nums,left,pivotIndex-1)
            self.quickSort2(nums,pivotIndex+1,right)
        return nums

    def heapSort(self,nums:List[int]):
        def adjustHeap(nums,i,size):
            lchild = 2*i+1
            rchild = 2*i+2
            largest = i
            if lchild<size and nums[lchild]>nums[largest]:
                largest = lchild
            if rchild<size and nums[rchild]>nums[largest]:
                largest = rchild
            if largest !=i:
                nums[largest],nums[i] = nums[i],nums[largest]
                adjustHeap(nums,largest,size)
        # 建立堆
        def builtHeap(nums,size):
            for i in range(len(nums)//2)[::-1]:
                adjustHeap(nums,i,size)

        size = len(nums)
        builtHeap(nums,size)
        for i in range(len(nums))[::-1]:
            nums[0],nums[i] = nums[i],nums[0]
            adjustHeap(nums,0,i)
        return nums

    def countingSort(self,nums):
        bucket = [0]*(max(nums)+1)
        for num in nums:
            bucket[num] += 1
        i = 0

        for j in range(len(bucket)):
            while bucket[j]>0:
                nums[i] = j
                bucket[j] -=1
                i+=1
        return nums

    def radixSort(nums): #基数排序 Python 代码实现
        mod = 10
        div = 1
        mostBit = len(str(max(nums)))  # 最大数的位数决定了外循环多少次
        buckets = [[] for row in range(mod)]  # 构造 mod 个空桶
        while mostBit:
            for num in nums:  # 将数据放入对应的桶中
                buckets[num // div % mod].append(num)
            i = 0  # nums 的索引
            for bucket in buckets:  # 将数据收集起来
                while bucket:
                    nums[i] = bucket.pop(0)  # 依次取出
                    i += 1
            div *= 10
            mostBit -= 1
        return nums


class solution:
    def topk(self, inputs, k):
        import heapq
        if inputs == None or len(inputs) < k or len(inputs) <= 0 or k <= 0:# 注意极限条件的确定
            return []
        output = []
        for number in inputs:
            if len(output) < k:
                output.append(number)
            else:
                output = heapq.nlargest(k, output)
                print(output)
                if number >= output[-1]:
                    output[-1] = number
                else:
                    continue
        return output









