def minDepth(self, root: TreeNode | None) -> int:
        
        def traverse(n, c):
            c += 1
            if n != None and n.left == None and n.right == None:
                return c
            if n == None:
                return -1
            
            l = traverse(n.left, c)
            r = traverse(n.right, c)
            
            if l < 0:
                return r
            if r < 0:
                return l

            return l if l < r else r
        
        a = traverse(root, 0)
        return a if a >= 0 else 0