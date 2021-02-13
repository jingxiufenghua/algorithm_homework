# Definition for singly-linked list.
from typing import List
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MylistNode:
    def __init__(self,l:ListNode=None):
        self.l = l
    def __eq__(self, other):
        return self.l.val==other.l.val
    def __lt__(self, other):
        return self.l.val<other.l.val
    def printlist(self):
        if self.l == None: return
        while self.l!= None:
            print(self.l.val, end='')
            self.l =self.l.next
    def append(self, other):
        listNode = ListNode(other)
        if self.is_empty():
            self.l = listNode
        else:
            cur = self.l
            while cur.next!=None:
                cur = cur.next
            cur.next = other
    def is_empty(self):
        return self.l  is None




class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummyhead = ListNode(0)
        curr = dummyhead
        heap =[MylistNode(i) for i in lists if i]
        heapq.heapify(heap)
        while heap:
            i = heapq.heappop(heap).l
            curr.next = ListNode(i.val)
            curr = curr.next
            if i.next:
                heapq.heappush(heap,MylistNode(i.next))
        return dummyhead.next

list1 = [1,4,5]
list2 = [1,3,4]
list3 = [2,6]

def list2MylistNode(List):
    head = ListNode(List[0])
    p = head
    for i in range(1,len(List)):
        p.next = ListNode(List[i])
        p = p.next
    return head

MylistNode1 = list2MylistNode(list1)
MylistNode2 = list2MylistNode(list2)
MylistNode3 = list2MylistNode(list3)

lists = [MylistNode1,MylistNode2,MylistNode3]
solution = Solution()
ListNode1 = solution.mergeKLists(lists)

cur = ListNode1
while cur!= None:
    print(cur.val)
    cur = cur.next
