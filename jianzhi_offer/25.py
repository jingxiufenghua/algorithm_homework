# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 : return l2
        if not l2 : return l1
        dummy= head = ListNode(0)
        head_1 = l1
        head_2 = l2
        while head_1 and head_2:
            if head_1.val<head_2.val:
                head.next = head_1
                head_1 = head_1.next
            else:
                head.next = head_2
                head_2 = head_2.next
            head = head.next
        head.next = head_1 if head_1 else head_2
        return dummy.next




