# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        right_node,left_node = dummy,dummy
        for i in range(right):
            right_node = right_node.next
        tail = prev = right_node.next
        for j in range(left-1):
            left_node = left_node.next
        up_node = left_node
        cur = left_node.next

        while cur != tail:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        up_node.next = prev

        return dummy.next
first = ListNode(5)
seconde = ListNode(4,first)
third = ListNode(3,seconde)
four = ListNode(2,third)
five = ListNode(1,four)

solution = Solution()
result = solution.reverseBetween(five,2,4)


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next



