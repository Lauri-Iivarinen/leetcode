#https://leetcode.com/problems/check-if-array-is-good/description/

class Solution:
    def isGood(self, nums) -> bool:
        occurrences = {}
        for num in nums:
            if num in occurrences:
                occurrences[num] = occurrences[num] + 1
            else:
                occurrences[num] = 1
        
        keys = list(occurrences.keys())
        keys.sort()
        if len(keys) + 1 == len(nums) and occurrences[keys[-1]] == 2 and keys[0] == 1 and keys[-1] == len(nums) - 1:
            return True
        return False

sol = Solution()

print(sol.isGood([2, 1, 3]))
print(sol.isGood([1, 3, 3, 2]))
print(sol.isGood([1, 1]))
print(sol.isGood([3, 4, 4, 1, 2, 1]))
