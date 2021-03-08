# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:return None
        stack = []
        stack.append(head)
        while head:
            next = head.next
            if next:
                stack.append(next)
            head = next
        if stack: res = head = stack.pop()
        while stack:
            next = stack.pop()
            head.next = next
            head = next
        head.next = None
        return res
# 循环写法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        cur=head
        while (cur!=None):
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        return prev

# 递归解法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur,prev):
            if cur==None: return prev #终止条件:如果cur为空，则开始回溯返回prev
            res=recur(cur.next,cur) #递归函数,往后遍历后继节点
            cur.next=prev #修改节点引用指向
            return res #返回res节点
        return recur(head,None)




