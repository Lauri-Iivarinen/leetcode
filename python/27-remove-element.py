def removeElement(self, nums: list[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


n = [3,2,2,3]
print(removeElement(None, n, 3))
print(n)