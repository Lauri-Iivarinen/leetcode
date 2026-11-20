class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
    # :D
    # return p == q

    def traverse_and_compare(p,q):
        if p == None or q == None:
            return p == q
        if p and q and p.val == q.val:
            if traverse_and_compare(p.left, q.left):
                return traverse_and_compare(p.right, q.right)
        return False

    return traverse_and_compare(p,q)




n = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
n2 = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), None)
n3 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, None)))
n3_2 = TreeNode(1, None, TreeNode(2, None, TreeNode(4, None, None)))

print(isSameTree(None, n,n))
print(isSameTree(None, n2,n2))
print(isSameTree(None, n3,n3))
print(isSameTree(None, n2,n3))
print(isSameTree(None, n3_2,n3))