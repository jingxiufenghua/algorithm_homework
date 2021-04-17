# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = res = ListNode()
        up_flag = 0
        while l1 or l2:
            first = l1.val   if l1 else 0
            second = l2.val  if l2 else 0
            cur = first + second + up_flag
            res.next = ListNode(cur%10)
            res = res.next
            up_flag = cur/10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if up_flag>0:
            res.next = ListNode(up_flag)
            res = res.next
        return head.next

solution = Solution()
# list1 = [9,9,9,9,9,9,9]
# list2 = [9,9,9,9]

list1 = [5]
list2 = [5]

def make_LinkList(list):
    if not list :return None
    head = ListNode(list[0])
    p = head
    for i in range(1,len(list)):
        p.next = ListNode(list[i])
        p = p.next
    return head

def print_LinkList(L:ListNode):
    if not L : return None
    while L:
        print(L.val)
        L = L.next

first_linklist = make_LinkList(list1)
second_linklist = make_LinkList(list2)

# print_LinkList(first_linklist)
# print_LinkList(second_linklist)

result = solution.addTwoNumbers(first_linklist,second_linklist)
print_LinkList(result)






