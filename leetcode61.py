# Definition for singly-linked list.
from leetcode_uitil import make_LinkList,print_LinkList
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:return None
        l,r = 1,1
        tail = head
        count = 0
        stack = []
        while tail:
            tail = tail.next
            count += 1
        move_step = k%count
        if move_step == 0 : return head

        tail = head
        while r<count-move_step:
            tail = tail.next
            r +=1
        temp = tail.next
        while temp:
            stack.append(temp.val)
            temp = temp.next

        tail.next=None

        while stack:
            new_node = ListNode(stack.pop())
            new_node.next = head
            head = new_node
        return head

solution = Solution()
nums = [1,2,3,4,5]
list = make_LinkList(nums)
result = solution.rotateRight(list,2)
print_LinkList(result)





