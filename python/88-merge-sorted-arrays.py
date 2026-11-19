def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(len(nums1)):
        print(nums1)
        if len(nums2) == 0:
            return
        if nums2[0] <= nums1[i]:
            nums1.insert(i, nums2.pop(0))
            nums1.pop()
            m += 1
        elif i >= m:
            v = nums2.pop(0)
            nums1[i] = v


nums1 = [1,2,3,0,0,0]
nums2 = [4,5,6]
#nums2 = [2,5,6]

#merge(None, nums1, 3, nums2, 3)
nums1 = [1]
merge(None, nums1, 1, [], 0)

print(nums1)