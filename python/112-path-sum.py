def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        def traverse(n, t):
            if n == None:
                return False
            if n.left == None and n.right == None:
                return t - n.val == 0
            
            if traverse(n.left, t-n.val) or traverse(n.right, t-n.val):
                return True
            return False

        return traverse(root, targetSum)