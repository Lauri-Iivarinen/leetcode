class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
    

    def gen_tree(arr):
       
        if len(arr) == 0 or arr == None:
            return None
        if len(arr) == 1:
           
            return TreeNode(arr[0])
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid+1:]
        #r = r[::-1]
        
        return TreeNode(arr[mid],gen_tree(l),gen_tree(r))

    return gen_tree(nums)

#a = sortedArrayToBST(None, [0,1,2])
a = sortedArrayToBST(None, [-10,-3,0,5,9])
print(a.left.val, a.val, a.right.val)