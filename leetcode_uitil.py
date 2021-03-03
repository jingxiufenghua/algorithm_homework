class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
