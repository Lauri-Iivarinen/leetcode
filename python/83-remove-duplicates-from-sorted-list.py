# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gen_ln(lst):
    l1 = None
    for v in lst:
        l1 = ListNode(v, l1)
    return l1

def print_list(l: ListNode):
    while l != None and l.val != None:
        print(l.val)
        l = l.next

def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
    curr = head
    while curr != None and curr.next != None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


# Turns out head DOES get modified in place lol
def deleteDuplicates_dumb(self, head: ListNode | None) -> ListNode | None:
    def reverse_list(n: ListNode):
        curr = None
        while n != None and n.val != None:
            curr = ListNode(n.val, curr)
            n = n.next
        return curr
    
    curr = None
    while head != None and head.val != None:
        print(head)
        if curr == None or (curr != None and curr.val != head.val):
            curr = ListNode(head.val, curr)
        head = head.next

    return reverse_list(curr)

l = [1,1,2,3,3]
l.reverse()

lst = gen_ln(l)
#print(lst)
#print_list(lst)
lst = deleteDuplicates(None, lst)
print()
print(lst)
print_list(lst)

