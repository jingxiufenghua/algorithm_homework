# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        save = []
        save.append(head)

        while head:
            next = head.next
            if next:
                if next in save:
                    return True
                else:
                    save.append(next)
            head = next
        return  False

