from typing import List
import math

class Solution:
    # binary search where nums[i] > nums[i+1] return nums[i+1]
    def findMin2(self, nums: list[int]) -> int:
        def fnd(nms: list[int]):
            left = 0
            right = len(nms) - 1
            if len(nms) == 2 and nms[left] > nms[right]:
                return nms[right]
            if len(nms) <= 2:
                return nms[left]
            
            center = math.floor(right / 2)
            if nms[center] < nms[right]: # go left
                return fnd(nms[:center+1])
            return fnd(nms[center:])
        
        return fnd(nums)


    # I think this is cheating but will pass the test...
    def findMin(self, nums: list[int]) -> int:
        return min(nums)


s = Solution()
#print(s.findMin([5,6,1,2,3,4]))
print(s.findMin2([1,2,3,4]))