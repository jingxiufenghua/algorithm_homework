# Definition for singly-linked list.
# 归并排序
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head:ListNode,tail:ListNode)->ListNode:
            if not head:return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast!=tail:
                slow = slow.next
                fast = fast.next
                if fast!= tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head,mid),sortFunc(mid,tail))
        def merge(head1:ListNode,head2:ListNode)->ListNode:
            dummyHead = ListNode()
            res = dummyHead
            while head1 and head2:
                if head1.val<=head2.val:
                    res.next = head1
                    head1 = head1.next
                else:
                    res.next = head2
                    head2 = head2.next
                res = res.next
            res.next = head1 or head2
            return dummyHead.next
        return sortFunc(head,None)








