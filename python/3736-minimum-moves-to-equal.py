import math
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        s = sum(nums)
        l = len(nums)

        return m * l - s
