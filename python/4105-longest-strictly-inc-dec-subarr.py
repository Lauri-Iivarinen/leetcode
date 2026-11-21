class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l,r = 0,0
        m = 0
        asc = True
        curr = 0
        while r < len(nums):
            if l == r:
                curr += 1
                if r == len(nums):
                    break
            elif nums[r-1] == nums[r]:
                l = r
                curr = 1
            elif asc and nums[r-1] < nums[r]:
                curr += 1
            elif not asc and nums[r-1] > nums[r]:
                curr += 1
            elif asc and nums[r-1] >= nums[r]:
                curr = 2
                asc = False
                l = r-1
            elif not asc and nums[r-1] <= nums[r]:
                curr = 2
                asc = True
                l = r-1 
            if curr > m:
                m = curr           
            r += 1
        
        return m if m > curr else curr
