def removeDuplicates(self, nums: list[int]) -> int:
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            nums.pop(i) # Does this slow down the process?
        else:
            i += 1
    return len(nums)

print(removeDuplicates(None, [1,1,2]))
print(removeDuplicates(None, [0,0,1,1,1,2,2,3,3,4]))