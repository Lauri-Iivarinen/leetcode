class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        def flatten(lst: ListNode):
            rst = []
            while lst != None and lst.val != None:
                rst.append(lst.val)
                lst = lst.next
            return rst

        def gen_ln(lst):
            l1 = None
            for v in lst:
                l1 = ListNode(v, l1)
            return l1

        
        mrg = []
        while list1 != None and list1.val != None and list2 != None and list2.val != None:
            if list1.val <= list2.val:
                mrg.append(list1.val)
                list1 = list1.next
            else:
                mrg.append(list2.val)
                list2 = list2.next

        if list1 != None:
            mrg = mrg + flatten(list1)
        if list2 != None:
            mrg = mrg + flatten(list2)

        mrg.reverse()
        return gen_ln(mrg)


# Helpers 

def gen_ln(lst):
    l1 = None
    for v in lst:
        l1 = ListNode(v, l1)
    return l1

def print_list(l: ListNode):
    while l != None and l.val != None:
        print(l.val)
        l = l.next

l1 = gen_ln([4,2,1])
l2 = gen_ln([4,3,1])

l3 = mergeTwoLists(None, l1, l2)


print()
print_list(l3)