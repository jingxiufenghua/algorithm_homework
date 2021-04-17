# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return  False
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        n = len(res)
        for i in range(n):
            if res[i] != res[n-i-1]:
                return False
        return True





