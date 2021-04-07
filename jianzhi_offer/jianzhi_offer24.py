# 剑指 Offer 24. 反转链表

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur :
            tmp = cur.next
            cur.next  = prev
            prev = cur
            cur = tmp
        return prev

# 剑指 Offer 18. 删除链表的节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val :return head.next
        pre,cur = head,head.next
        while cur and cur.next.val!=val:
            pre,cur = cur,cur.next
        if cur:pre.next = cur.next
        return head



