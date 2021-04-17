# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        save = {}
        save[head] = 1
        while head:
            next = head.next
            if next:
                if save.get(next):
                    return True
                else:
                    save[next] = 1
            head = next
        return None
