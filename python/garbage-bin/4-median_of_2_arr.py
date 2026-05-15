import math

# The overall run time complexity should be O(log (m+n)).
class Solution:

    # this is shit
    # # some edge cases cannot be determined by math
    # def findMedianSortedArrays3(self, nums1: list[int], nums2: list[int]) -> float:
    #     def median(nums):
    #         if len(nums) % 2 == 0:
    #             return (nums[int(len(nums)/2)] + nums[int(len(nums)/2-1)]) / 2
    #         return nums[math.floor(len(nums)/2)]
    #     if len(nums1) > 0 and len(nums2) > 0:
    #         return (median(nums1) + median(nums2)) / 2
    #     if len(nums1) > 0 and len(nums2) == 0:
    #         return median(nums1)
    #     if len(nums1) == 0 and len(nums2) > 0:
    #         return median(nums2)
    #     return 0


    # also shit because too complex
    # sort makes it so its not in correct time complexity
    def findMedianSortedArrays2(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()

        if len(nums) % 2 == 0:
            return (nums[int(len(nums)/2)] + nums[int(len(nums)/2-1)]) / 2
        
        return nums[math.floor(len(nums)/2)]


s = Solution()

print(s.findMedianSortedArrays([2,2,4,4],[2,2,2,4,4]))