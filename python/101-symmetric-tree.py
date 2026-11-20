def isSymmetric(self, root: TreeNode | None) -> bool:
    if root.left == None or root.right == None:
        return root.left == root.right
    
    la = []
    ra = []
    
    def traverse_r(n):
        if n == None:
            return
        ra.append(n.right.val if n.right != None else None)
        traverse_r(n.right)
        ra.append(n.val)
        ra.append(n.left.val if n.left != None else None)
        traverse_r(n.left)
        
    
    def traverse_l(n):
        if n == None:
            return
        la.append(n.left.val if n.left != None else None)
        traverse_l(n.left)
        la.append(n.val)
        la.append(n.right.val if n.right != None else None)
        traverse_l(n.right)
    
    traverse_l(root.left)
    traverse_r(root.right)
    
    #print(la)
    #print(ra)
    
    return la == ra
