# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 超出时间限制
class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     stack = []
    #     while headA:
    #         stack.append(headA)
    #         headA = headA.next
    #     while headB:
    #         if headB in stack:
    #             return headB
    #         else:
    #             headB = headB.next
    #     return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:return None
        pa = headA
        pb = headB
        while pa!=pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headB or not headA: return None
        pa = headA
        pb = headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa

