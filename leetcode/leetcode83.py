# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head :return  None
        dummy = ListNode()
        dummy.next = head
        cur = head
        while cur:
            second = cur.next
            while second and second.val == cur.val:
                    second = second.next
            cur.next = second
            cur = second
        return head

first = ListNode(5)
seconde = ListNode(4,first)
third = ListNode(3,seconde)
four = ListNode(1,third)
five = ListNode(1,four)

solution = Solution()
result = solution.deleteDuplicates(five)
