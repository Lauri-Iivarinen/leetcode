class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(self, root: TreeNode | None) -> list[int]:
    ar = []
    def traverse(root):
        if root == None:
            return
        traverse(root.left)
        ar.append(root.val)
        traverse(root.right)
    
    traverse(root)
    return ar


# some mishap in logic does not work
def inorderTraversal_iter(self, root: TreeNode | None) -> list[int]:
    res = []
    proc = [root]
    c = 0
    while True and c < 5:
        curr = proc[-1]
        print(curr.val)
        if curr.left == None:
            res.append(curr.val)
            print("left resolved, ", res)
            proc.pop()

            if curr.right != None:
                proc.append(curr.right)

    return res


n = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
print(inorderTraversal_iter(None, n))