class Solution:

    # using brain
    def getCommon(self, nums1, nums2):
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1

        
    # braindead over-engineering
    def getCommon2(self, nums1: list[int], nums2: list[int]) -> int:
        def bin_search(nums: list[int], val: int):
            #print(v, nums)
            left = 0
            right = len(nums)-1
            if right == 0:
                return nums[0] == val
            if right == 1:
                return nums[left] == val or nums[right] == val
            
            center = right // 2
            if nums[center] == val:
                return True
            if nums[center] > val:
                return bin_search(nums[:center], val)
            return bin_search(nums[center+1:], val)

        if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]:
            return -1
            
        for v in nums1:
            if bin_search(nums2, v):
                return v
        
        return -1


t = Solution()

print(t.getCommon([1,2,3], [2,4]))