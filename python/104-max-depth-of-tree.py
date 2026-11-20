def maxDepth(self, root: TreeNode | None) -> int:
    def traverse(n, c):
        if n == None:
            return c
        c += 1
        lc = traverse(n.left, c)
        rc = traverse(n.right, c)
    
        return rc if rc > lc else lc
    
    return traverse(root, 0)
