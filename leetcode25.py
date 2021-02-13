# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dumb = ListNode(10086)
        dumb.next = head
        end = prev = dumb
        def swap(prev,k,end):
            after = end.next
            move = prev.next
            prev.next = end
            temp = move.next
            end = move
            for  i in range(k-1):
                tnext = temp.next
                temp.next = move
                move = temp
                temp = tnext
            end.next = after
            return end
        while True:
            try:
                for _ in range(k):
                    end = end.next
                prev = end = swap(prev,k,end)
            except:
                break
        return dumb.next