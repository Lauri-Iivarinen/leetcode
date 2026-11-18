def dumbass_lauri_doesnt_remember_binary_search_searchInsert(self, nums: list[int], target: int) -> int:
    if len(nums) == 0:
        return 0
    l = 0
    r = len(nums) - 1
    while True:
        # pos found or indexes are next to each other
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        if l+1 == r:
            if nums[r] < target:
                return r + 1
            elif nums[l] > target: # can this even trigger
                return l
            elif nums[r] > target:
                return r
        if l == r:
            if  nums[r] > target:
                return r
            else:
                return r+1

        if nums[l + (r-l)//2] >= target:
            r = l + (r-l)//2
        else:
            l = l + (r-l)//2



def searchInsert(self, nums: list[int], target: int) -> int:

    def bs(nums,l,r,t):
        print(l,r,t)
        m = l + (r - l) // 2
        if nums[m] == t:
            return m
        if l + 1 >= r:
            if t < nums[l]:
                return l
            if t > nums[r]:
                return r + 1
            return r
        
        if nums[m] <= t:
            return bs(nums,m,r,t)
        return bs(nums,l,m,t)

    l = 0
    r = len(nums) - 1
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 0 if nums[0] >= target else 1

    return bs(nums,l,r,target)








v = [1,2,3,4,5,6]
v2 = [1,2,3]

print(searchInsert(None, [1,3,5,6], 2))
#print(searchInsert(None, v2, 1))