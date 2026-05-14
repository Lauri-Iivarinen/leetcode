#https://leetcode.com/problems/add-two-numbers/description/

#Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def get_num(l: ListNode):
        num: List[str] = [str(l.val)]
        curr = l
        while curr.next != None:
            curr = curr.next
            num.append(str(curr.val))
        
        num.reverse()
        return int("".join(num))
    
    out = get_num(l1) + get_num(l2)
    ans = list(map(int, list(str(out))))
    #ans.reverse()
    #a = None
    prev = None
    for val in ans:
        prev = ListNode(val, prev)

    return prev


a = addTwoNumbers(None, ListNode(1, ListNode(2)), ListNode(2, ListNode(3)))
print(a)