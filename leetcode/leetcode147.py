# Definition for singly-linked list.
# 选择排序
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        lastSort = head
        curr =head.next
        while curr:
            if lastSort.val<=curr.val:
                lastSort =lastSort.next
            else:
                prev = dummyNode
                while prev.next.val<=curr.val:
                    prev = prev.next
                lastSort.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSort.next
        return dummyNode.next

